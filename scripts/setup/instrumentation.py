'''
Generates solcmc contracts from versions and properties files.
'''

from setup import injector
from pathlib import Path
import logging
import utils
import sys
import re


TAG_GHOSTSTATE = '/// @custom:ghost'
TAG_PREGHOST = '/// @custom:preghost'
TAG_POSTGHOST = '/// @custom:postghost'
TAG_INVARIANT = '/// @custom:invariant'


def get_ghost(lines, i):
    '''
    Yields the code until EOF or '///'.
    Returns the code and the new index.
    '''
    code = [lines[i-1]]     # Save tag

    while i < len(lines) and not any(
            [TAG_GHOSTSTATE in lines[i],
             TAG_PREGHOST in lines[i],
             TAG_POSTGHOST in lines[i],
             TAG_INVARIANT in lines[i]]):

        code.append(lines[i])
        i += 1

    return code, i


def get_ghosts(property_path: str) -> dict:
    '''
    Extracts the ghost code from a solcmc property file.
    '''

    ghosts = {
            'pre': {},
            'post': {},
            'state': [],
            'invariants': []
            }

    # Support old specifications, to be removed later
    with open(property_path, 'r') as f:
        code = f.read()

        state_match = re.search(TAG_GHOSTSTATE, code)
        pre_match = re.search(TAG_PREGHOST + ' (.*)', code)
        post_match = re.search(TAG_POSTGHOST + ' (.*)', code)
        inv_match = re.search(TAG_INVARIANT, code)

        if not any([state_match, pre_match, post_match, inv_match]) and len(code) > 0:
            if code.strip():
                ghosts['invariants'].append([l + '\n' for l in code.splitlines()])
                return ghosts

    # Yield verification ghosts
    with open(property_path, 'r') as f:
        lines = f.readlines()
        i = 0
        header_collected = False   # To collect header
        header = []

        while i < len(lines):
            line = lines[i]

            ''' This is very inefficient '''
            # Look for a tag in the current line
            state_match = re.search(TAG_GHOSTSTATE, line)
            pre_match = re.search(TAG_PREGHOST + ' (.*)', line)
            post_match = re.search(TAG_POSTGHOST + ' (.*)', line)
            inv_match = re.search(TAG_INVARIANT, line)

            if state_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                state, i = get_ghost(lines, i+1)
                ghosts['state'] += header + state
            elif pre_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save function name and preghosts
                fun = pre_match.group(1).strip()
                precond, i = get_ghost(lines, i+1)
                ghosts['pre'][fun] = header + precond
            elif post_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save function name and postghosts
                fun = post_match.group(1).strip()
                postcond, i = get_ghost(lines, i+1)
                ghosts['post'][fun] = header + postcond
            elif inv_match:
                if not header_collected:
                    header_collected = True
                    header = lines[:i]
                # Save invariants
                inv, i = get_ghost(lines, i+1)
                ghosts['invariants'] += [header + inv]
            else:
                i += 1

            if header:
                header = []

    return ghosts


def instrument_contracts(versions_paths: list, properties_paths: list) -> dict:
    '''
    Instruments contracts to verify from versions and properties.
    They will go to build/contracts.

    Returns:
        dict: { filename: contract_code, ...}
    '''

    contracts = {}

    for version_path in versions_paths:
        # Get list of properties to verify for this version
        version_properties_paths = utils.get_properties(version_path, properties_paths)

        # Instrument version for every property
        for property_path in version_properties_paths:

            contract = []   # contract to instrument
            with open(version_path, 'r') as f:
                contract = f.readlines()

            ghosts = get_ghosts(property_path)

            ''' Move this into another function '''
            # Empty property file
            if not any(ghosts[key] for key in ['state', 'pre', 'post', 'invariants']):
                logging.warning(f'No instrumentation found in {property_path}.')

            if ghosts['state']:
                # Inject before last bracket
                contract_pattern = 'contract ' + utils.get_contract_name(version_path)
                contract = injector.inject_after(contract, ghosts['state'], contract_pattern)
                if contract is None:
                    state = ''.join(l for l in code)
                    logging.error(f'Ghost state injection failed: {property_path}: '
                                  f'{version_path}: {state}.')
                    sys.exit(1)

            for fun, code in ghosts['pre'].items():
                # Inject after function signature
                contract = injector.inject_after(contract, code, fun)
                if contract is None:
                    logging.error(
                            f'Preghost injection failed: {property_path}: '
                            f'{version_path}: {fun}.')
                    sys.exit(1)

            for fun, code in ghosts['post'].items():
                # Inject before last bracket of function
                contract = injector.inject_postcond(contract, code, fun)
                if contract is None:
                    logging.error(
                            f'Postghost injection failed: {property_path}: '
                            f'{version_path}: {fun}.')
                    sys.exit(1)

            for inv in ghosts['invariants']:
                # Inject before last bracket
                contract = injector.inject_before_last_bracket(contract, inv)
                if contract is None:
                    inv_as_string = ''.join(l for l in inv)
                    logging.error(f'Invariant injection failed: {property_path}: '
                                  f'{version_path}: {inv_as_string}.')
                    sys.exit(1)

            # Construct filename
            name, version_id = Path(version_path).stem.split('_')
            property_id = Path(property_path).stem
            filename = f'{name}_{property_id}_{version_id}.sol'

            contracts.update({filename: ''.join(l for l in contract)})

    return contracts
