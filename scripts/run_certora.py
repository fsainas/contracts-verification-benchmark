'''
Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -c <file_or_dir> -s <spec_file> -o <output_dir>
'''

from string import Template
from multiprocessing import Pool
import subprocess
import argparse
import logging
import utils
from utils import (
        STRONG_POSITIVE,
        STRONG_NEGATIVE,
        WEAK_POSITIVE,
        WEAK_NEGATIVE,
        NONDEFINABLE,
        ERROR
        )
import glob
import sys
import os
import re

THREADS = 6     # n of parallel executions


COMMAND_TEMPLATE = Template(
    'certoraRun $contract_path:$name --verify $name:$spec_path --msg "$msg"  --wait_for_results'
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
    with open(spec_path, 'r') as file:
        spec_code = file.read()
        spec_no_comments = utils.remove_comments(spec_code)

        has_satisfy = re.search('satisfy', spec_no_comments)
        has_assert = re.search('assert', spec_no_comments)

        # Check if there are asserts or satisfy
        if not has_assert and not has_satisfy:
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

    try:
        contract = contract_path.split('/')[-1].split('.')[0].split('_')
        contract = contract[0]+contract[2]
    except:
        contract = contract_path.split('/')[-1].split('.')[0]
    spec = spec_path.split('/')[-1].split('.')[0] 

    params['msg'] = contract + "/" + spec

    command = COMMAND_TEMPLATE.substitute(params)
    print(command)
    log = subprocess.run(command.split(), capture_output=True, text=True)


    # Handle Certora errors
    if log.stderr:
        print(log.stderr, file=sys.stderr)

    if has_critical_error(log.stdout):
        logging.error(log.stdout)
        return ERR, log.stdout

    # Save result
    is_positive = no_errors_found(log.stdout)
    # Negation
    is_positive = not is_positive if negate else is_positive

    res = STRONG_POSITIVE if has_assert else WEAK_POSITIVE
    if not is_positive:
        res = WEAK_NEGATIVE if has_assert else STRONG_NEGATIVE

    print(f'{contract_path}, {spec_path}: {res}')
    return res, f'{log.stdout}\n\n{log.stderr}'


def run_log(id, contract_path, spec_path, logs_dir=None):
    '''
    Calls run() and writes the log.
    '''
    outcome, log = run(contract_path, spec_path)
    if logs_dir:
        utils.write_log(logs_dir + id + '.log', log)
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

    # Specific properties
    bound_properties_paths = list(filter(
            lambda x: re.search(".*_v.*", x),
            specs_paths))
    unbound_properties_paths = list(
            set(specs_paths) - set(bound_properties_paths))

    inputs = []     # inputs for run_log()

    for v_path in contracts_paths:
        # Extract base id from base path (e.g. v1)
        v_id = v_path.split('/')[-1].split('_')[-1].split('.')[0]

        v_bound = list(filter(
                lambda x: re.search(f'.*_{v_id}.*', x),
                bound_properties_paths))

        v_unbound = unbound_properties_paths

        for bp_path in v_bound:
            p_id = bp_path.split('/')[-1].split('_')[0]     # ../p1_v1.sol -> p1
            # Remove bound properties from the unbound variants
            v_unbound = list(filter(
                    lambda x: not re.search(f'{p_id}', x),
                    v_unbound
                    ))

        # List of properties to test for the current version
        v_properties_paths = v_bound + v_unbound

        for s_path in v_properties_paths:
            id = (  # e.g. p1_v1
                    s_path.split('.')[-2].split('/')[-1].split('_')[0] +
                    '_' +
                    v_path.split('_')[-1].split('.sol')[0]
            )
            inputs.append((id, v_path, s_path, logs_dir))

    with Pool(processes=THREADS) as pool:
        # [(id, outcome), ...]
        results = pool.starmap(run_log, inputs)
        for id, outcome in results:
            outcomes[id] = outcome

    return outcomes


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contracts',
            '-c',
            help='Contracts dir or contract file.',
            required=True
            )
    parser.add_argument(
            '--specs',
            '-s',
            help='CVL Specification dir or file.',
            required=True
            )
    parser.add_argument(  # build/
            '--output',
            '-o',
            help='Output directory.',
            #required=True
    )
    args = parser.parse_args()

    # Remove final slash
    contracts = (
            args.contracts
            if args.contracts[-1] != '/'
            else args.contracts[:-1]
            )

    # Get contracts paths
    contracts_paths = (
            glob.glob(f'{contracts}/*.sol')
            if os.path.isdir(contracts)
            else [contracts]
    )

    # Remove final slash
    specs = (
            args.specs
            if args.specs[-1] != '/'
            else args.specs[:-1]
            )

    # Get specs paths
    specs_paths = (
            glob.glob(f'{specs}/*.spec')
            if os.path.isdir(specs)
            else [specs]
    )

    if args.output:
        output_dir = args.output if args.output[-1] == '/' else args.output + '/'
        logs_dir = output_dir + 'logs/'

        outcomes = run_all(contracts_paths, specs_paths, logs_dir)

        out_csv = [utils.OUT_HEADER]
        for id in outcomes.keys():
            p = id.split('_')[0]
            v = id.split('_')[1]
            out_csv.append([p, v, outcomes[id]])

        utils.write_csv(output_dir + 'out.csv', out_csv)
    else:
        run_all(contracts_paths, specs_paths)
