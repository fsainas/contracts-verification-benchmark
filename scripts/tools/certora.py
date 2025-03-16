'''
Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -c <file_or_dir> -s <spec_file> -o <output_dir>
'''

from string import Template
from multiprocessing import Pool
from pathlib import Path
import subprocess
import logging
import sys
import os
import re

import utils
from utils import (STRONG_POSITIVE,
                   STRONG_NEGATIVE,
                   WEAK_POSITIVE,
                   WEAK_NEGATIVE,
                   NONDEFINABLE,
                   ERROR)

THREADS = 6     # n of parallel executions


COMMAND_TEMPLATE = Template(
    'certoraRun $contract_path:$name --verify $name:$spec_path --msg "$msg" --wait_for_results'
)

CONF_FILE_COMMAND_TEMPLATE = Template(
    'certoraRun $conf_path --wait_for_results'
)

# Check if there is an error in the output (Deprec)
def has_property_error(output, property):
    pattern = rf'.*ERROR: \[rule\] {re.escape(property).upper()}.*'
    return re.search(pattern, output, re.DOTALL)


def no_errors_found(output):
    pattern = r'.*No errors found by Prover!.*'
    return re.search(pattern, output, re.DOTALL)


def has_critical_error(output):
    pattern = r'.*CRITICAL.*'
    return re.search(pattern, output, re.DOTALL)

def no_permission(output):
    """ Parse the output looking for a no permission error. """
    pattern = r'.*You have no permission.*'
    return re.search(pattern, output, re.DOTALL)


def run(contract_path, spec_path):
    '''
    Runs a single certora experiment.

    Returns:
        tuple: (outcome, log)
    '''

    # Check if the contract to verify exists
    if not os.path.isfile(contract_path):
        msg = f'{contract_path} not found.'
        logging.error(msg)
        return ERROR, msg

    # Name of the Solidity contract to verify
    contract_name = utils.get_contract_name(contract_path)

    # Check the contract name
    if not contract_name:
        msg = f'Could not retrieve {contract_path} contract name.'
        logging.error(msg)
        return ERROR, msg

    # Process specs file
    negate = False
    has_satisfy = False
    has_assert = False
    has_invariant = False
    with open(spec_path, 'r') as file:
        spec_code = file.read()
        spec_no_comments = utils.remove_comments(spec_code)

        has_satisfy = re.search('satisfy', spec_no_comments)
        has_assert = re.search('assert', spec_no_comments)
        has_invariant = re.search('invariant', spec_no_comments)

        # Check if there are asserts or satisfy
        if not has_assert and not has_satisfy and not has_invariant:
            msg = f'Error in {spec_path}: No "assert" or "satisfy" found.'
            logging.error(msg)
            return ERROR, msg

        # Exit if both are used
        if has_assert and has_satisfy:
            msg = f'Error in {spec_path}: Combining both "satisfy" and "assert" is not allowed.'
            logging.error(msg)
            return ERROR, msg

        # Process tags
        # Tag Nondefinable
        nondef = re.search('/// @custom:nondef (.*)', spec_code)
        if nondef:
            print(f'{contract_path}: {NONDEFINABLE} (nondefinable)')
            return NONDEFINABLE, nondef.group(1)

        # Tag Negate
        negate = re.search('/// @custom:negate', spec_code)


    # Prepare to fill template command
    params = {}
    params['contract_path'] = contract_path
    params['name'] = contract_name
    params['spec_path'] = spec_path
    name, version_id = Path(contract_path).stem.split('_')
    property_id = Path(spec_path).stem.split('_')[0]
    params['msg'] = f'{name}_{property_id}_{version_id}'
    
    conf_params = {}
    conf_params['conf_path'] = f'certora/conf/{property_id}.conf'
    conf_command = CONF_FILE_COMMAND_TEMPLATE.substitute(conf_params)

    if os.path.isfile(conf_params['conf_path']):
        try:
            log = subprocess.run(conf_command.split(), capture_output=True, text=True)
        except FileNotFoundError as e:
            if 'certoraRun' in str(e):
                logging.error('Certora is not installed. Use:\npip install certora-cli.')
                return ERROR, str(e)
    else:
        command = COMMAND_TEMPLATE.substitute(params)
        # print(command) - substitute with a log that does not go to stdout
        try:
            log = subprocess.run(command.split(), capture_output=True, text=True)
        except FileNotFoundError as e:
            if 'certoraRun' in str(e):
                logging.error('Certora is not installed. Use:\npip install certora-cli.')
                return ERROR, str(e)
    
    # Handle Certora errors
    if log.stderr:
        print(log.stderr, file=sys.stderr)

    if has_critical_error(log.stdout):
        logging.error(log.stdout)
        return ERROR, log.stdout

    if no_permission(log.stdout):
        logging.error(log.stdout)
        return ERROR, log.stdout

    # Save result
    is_positive = no_errors_found(log.stdout)
    # Negation
    is_positive = not is_positive if negate else is_positive

    res = STRONG_POSITIVE if has_assert or has_invariant else WEAK_POSITIVE
    if not is_positive:
        res = WEAK_NEGATIVE if has_assert or has_invariant else STRONG_NEGATIVE

    print(f'{contract_path}, {spec_path}: {res}')
    return res, f'{log.stdout}\n\n{log.stderr}'


def run_log(id, contract_path, spec_path, logs_dir=None):
    '''
    Calls run() and writes the log.
    '''
    outcome, log = run(contract_path, spec_path)
    if logs_dir:
        utils.write_log(Path(logs_dir).joinpath(id + '.log'), log)
    else:
        print(log)
        print(f'Result: {outcome}') 
    return id, outcome


def run_all(contracts_paths, specs_paths, logs_dir=None):
    '''
    Runs certora on all files of a directory.

    Args:
        contracts_paths (list): Contracts paths.
        specs_paths (list): CVL specs paths.
        log_dir (str): Log directory path.

    Returns:
        dict: {key_v*: outcome}
    '''
    outcomes = {}
    inputs = []     # inputs for run_log()

    for contract_path in contracts_paths:
        # Get list of properties to verify for this contract
        contract_properties_paths = utils.get_properties(contract_path, specs_paths)

        for property_path in contract_properties_paths:
            property_id = Path(property_path).stem.split('_')[0]    # split to eventually remove version
            version_id = Path(contract_path).stem.split('_')[1]
            id = f'{property_id}_{version_id}'
            inputs.append((id, contract_path, property_path, logs_dir))

    with Pool(processes=THREADS) as pool:
        # [(id, outcome), ...]
        results = pool.starmap(run_log, inputs)
        for id, outcome in results:
            outcomes[id] = outcome

    return outcomes
