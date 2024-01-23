'''
Generates solcmc contracts from versions and properties files.

Usage:
    python builder.py -b <versions_path>
    -i <properties_path> [-o <output_dir>]
'''

import injector
import argparse
import logging
from pathlib import PurePath
import glob
import sys
import os
import re

TAG_PRECOND = '/// @custom:precond'
TAG_POSTCOND = '/// @custom:postcond'
TAG_INVARIANT = '/// @custom:invariant'


def get_condition(lines, i):
    '''
    Yields the code until EOF or '///'.
    Returns the code and the new index.
    '''
    code = [lines[i-1]]     # Save tag

    while i < len(lines) and not any([
        TAG_PRECOND in lines[i],
        TAG_POSTCOND in lines[i],
        TAG_INVARIANT in lines[i]]):

        code.append(lines[i])
        i += 1

    return code, i


def get_conditions(property_path):
    '''
    Extracts the conditions from a solcmc property file.
    Returns:
        dict: {
            'preconditions': {},
            'postconditions': {},
            'invariants': []
            }
    '''

    conditions = {
            'preconditions': {},
            'postconditions': {},
            'invariants': []
            }

    # Support old specifications, to be removed later
    with open(property_path, 'r') as f:
        prop = f.read()

        precond_match = re.search(TAG_PRECOND+' (.*)', prop)
        postcond_match = re.search(TAG_POSTCOND+' (.*)', prop)
        inv_match = re.search(TAG_INVARIANT, prop)

        if not any([precond_match,
                    postcond_match,
                    inv_match]) and len(prop) > 0:
            conditions['invariants'].append(l + '\n' for l in prop.splitlines())
            return conditions

    # Yield verification conditions
    with open(property_path, 'r') as f:
        lines = f.readlines()
        i = 0
        header_collected = False   # To collect header
        header = []

        while i < len(lines):
            line = lines[i]

            precond_match = re.search(TAG_PRECOND+' (.*)', line)
            postcond_match = re.search(TAG_POSTCOND+' (.*)', line)
            inv_match = re.search(TAG_INVARIANT, line)

            if precond_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save function name and preconditions
                fun = precond_match.group(1).strip()
                precond, i = get_condition(lines, i+1)
                conditions['preconditions'][fun] = header + precond
            elif postcond_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save function name and postconditions
                fun = postcond_match.group(1).strip()
                postcond, i = get_condition(lines, i+1)
                conditions['postconditions'][fun] = header + postcond
            elif inv_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save invariants
                inv, i = get_condition(lines, i+1)
                conditions['invariants'] = [header + inv]
            else:
                i += 1

            if header:
                header = []

    return conditions


def build_contracts(versions_paths: list, properties_paths: list) -> dict:
    '''
    Builds contracts to verify from versions and properties.
    They will go to build/contracts.

    Returns:
        dict: { filename: contract_code, ...}
    '''

    '''IMPROVEMENT 
    Move properties sorting in a separate function '''
    # Properties associated with a version
    specific_properties = list(filter(
            lambda x: re.search(".*_v.*", x),
            properties_paths))

    # Generic properties
    generic_properties = list(
            set(properties_paths) - set(specific_properties))

    contracts = {}

    for v_path in versions_paths:
        # Extract base id from base path (e.g. v1)
        v_id = PurePath(v_path).stem.split('_')[1]

        # Properties associated with the current version v
        v_specific_properties = list(filter(
                lambda x: re.search(f'.*_{v_id}.*', x),
                specific_properties))

        v_generic_properties = generic_properties

        # Remove bound properties from the unbound variants
        for specific_property in v_specific_properties:
            # ../p1_v1.sol -> p1
            p_id = PurePath(specific_property).stem.split('_')[0]

            v_generic_properties = list(filter(
                    lambda x: not re.search(f'{p_id}', x),
                    v_generic_properties
                    ))

        # List of properties to verify for the current version
        v_properties_paths = v_specific_properties + v_generic_properties

        # Instrument version for every property
        for property_path in v_properties_paths:

            contract = []   # contract to instrument
            with open(v_path, 'r') as f:
                contract = f.readlines()

            conditions = get_conditions(property_path)

            if not any([conditions['preconditions'],
                       conditions['postconditions'],
                       conditions['invariants']]):
                logging.warning(f'No instrumentation found in {property_path}.')

            for fun, code in conditions['preconditions'].items():
                # Inject after function signature
                contract = injector.inject_after(contract, code, fun)
                if contract is None:
                    logging.error(
                            f'Precondition injection failed: {property_path}: '
                            f'{v_path}: {fun}.')
                    sys.exit(1)

            for fun, code in conditions['postconditions'].items():
                # Inject before last bracket of function
                contract = injector.inject_postcond(contract, code, fun)
                if contract is None:
                    logging.error(
                            f'Postcondition injection failed: {property_path}: '
                            f'{v_path}: {fun}.')
                    sys.exit(1)

            for inv in conditions['invariants']:
                # Inject before last bracket
                contract = injector.inject_before_last_bracket(contract, inv)
                if contract is None:
                    inv_as_string = ''.join(l for l in inv)
                    logging.error(f'Invariant injection failed: {property_path}: '
                                  f'{v_path}: {inv_as_string}.')
                    sys.exit(1)

            # Construct filename
            name = PurePath(v_path).stem.split('_')[0]
            p_id = PurePath(property_path).stem
            filename = f'{name}_{p_id}_{v_id}.sol'

            contracts.update({filename: ''.join(l for l in contract)})

    return contracts


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--versions',
            '-v',
            help='Version file or dir path.',
            required=True
    )
    parser.add_argument(
            '--properties',
            '-p',
            help='Property file or dir path.',
            required=True
    )
    parser.add_argument(
            '--output',
            '-o',
            help='Output directory path.',
    )
    args = parser.parse_args()

    if args.output:
        args.output = args.output if args.output[-1] == '/' else args.output + '/'

    args.versions = (
            args.versions 
            if args.versions[-1] != '/'
            else args.versions[:-1]
            )

    args.properties = (
            args.properties 
            if args.properties[-1] != '/'
            else args.properties[:-1]
            )

    versions_paths = (
            glob.glob(f'{args.versions}/*v*.sol')
            if os.path.isdir(args.versions)
            else [args.versions]
    )

    properties_paths = (
            glob.glob(f'{args.properties}/*.sol')
            if os.path.isdir(args.properties)
            else [args.properties]
    )

    contracts = build_contracts(
            versions_paths,
            properties_paths
    )

    for name in contracts.keys():
        if args.output:
            with open(args.output + name, 'w') as file:
                file.write(contracts[name])
        else:
            print(contracts[name])
