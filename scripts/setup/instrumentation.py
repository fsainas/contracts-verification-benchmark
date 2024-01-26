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


def get_ghost(lines: list, i: int) -> tuple:
    '''
    Extracts code until EOF or '///', returning the code and the new index.

    Args:
        lines (list): List of lines containing the code.
        i (int): Index indicating the starting position for code extraction.

    Returns:
        tuple: A tuple containing the extracted code as a list of lines and the
        updated index.
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
    Extracts ghost code from a solcmc property file.

    Args:
        property_path (str): The path to the solcmc property file.

    Returns:
        dict: A dictionary containing preghosts, postghosts, state ghosts, and invariants.
              Structure: {'pre': {function_name: [code_lines, ...]},
                          'post': {function_name: [code_lines, ...]},
                          'state': [code_lines, ...],
                          'invariants': [[code_lines, ...]]}

    Note:
        This function processes a solcmc property file, collecting code
        sections labeled as preghosts, postghosts, state ghosts, and
        invariants. The collected code is organized into a dictionary. If the
        property file is empty or lacks the specified tags, it returns an empty
        dictionary.
        The function relies on the get_ghost helper function for extracting
        ghost code sections.

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

    # Empty property
    if not code.strip():
        return ghosts

    tags_in_code = [TAG_PREGHOST in code, 
                    TAG_POSTGHOST in code, 
                    TAG_GHOSTSTATE in code, 
                    TAG_INVARIANT in code]

    if not any(tags_in_code):
        ghosts['invariants'].append([l + '\n' for l in code.splitlines()])
        return ghosts

    # Yield verification ghosts
    with open(property_path, 'r') as f:
        lines = f.readlines()

    header_collected = False   # To collect header
    header = []
    i = 0
    while i < len(lines):
        line = lines[i]

        tags_in_line = [TAG_PREGHOST in line, 
                        TAG_POSTGHOST in line, 
                        TAG_GHOSTSTATE in line, 
                        TAG_INVARIANT in line]
        
        if any(tags_in_line):
            if not header_collected:
                header_collected = True
                header = lines[:i]

        if TAG_PREGHOST in line:
            # Save function name and preghosts
            fun = re.search(TAG_PREGHOST + ' (.*)', line).group(1).strip()
            precond, i = get_ghost(lines, i+1)
            ghosts['pre'][fun] = header + precond
        elif TAG_POSTGHOST in line:
            # Save function name and postghosts
            fun = re.search(TAG_POSTGHOST + ' (.*)', line).group(1).strip()
            postcond, i = get_ghost(lines, i+1)
            ghosts['post'][fun] = header + postcond
        elif TAG_GHOSTSTATE in line:
            state, i = get_ghost(lines, i+1)
            ghosts['state'] += header + state
        elif TAG_INVARIANT in line:
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
