"""
Operates on either a single file or every file within a directory.

Usage:
    python run_solcmc.py -i <file_or_dir> -o <output_dir> [-t <timeout>]
"""

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
import sys
import re
import os

DEFAULT_TIMEOUT = '10m'
THREADS = 6

COMMAND_TEMPLATE = Template(
        'timeout $timeout ' + 
        'solc $contract_path ' +
        '--model-checker-engine chc ' +
        '--model-checker-timeout 0 ' +
        '--model-checker-targets assert ' +
        '--model-checker-show-unproved'
)


def has_error(output):
    pattern = r'.*Error:.*'
    return re.search(pattern, output, re.DOTALL)


def has_source_error(output):
    pattern = r'.*Error: Source.*'
    return re.search(pattern, output, re.DOTALL)


def has_assertion_warning(output):
    pattern = r'.*Warning: CHC: Assertion violation happens here.*'
    return re.search(pattern, output, re.DOTALL)


def is_timeout_or_unknown(output):
    pattern = r'.*Warning: CHC: Assertion violation might happen here.*'
    return re.search(pattern, output, re.DOTALL)


def run(contract_path, timeout):
    """
    Runs a single solcmc experiment.

    Returns:
        tuple: (outcome, log)
    """
    # File not found
    if not os.path.isfile(contract_path): 
        msg = f'{contract_path} not found.'
        logging.error(msg)
        return (ERROR, msg)

    negate = False
    with open(contract_path, 'r') as file:
        contract_code = file.read()

        # Process tags
        # Tag Nondefinable
        nondef = re.search('/// @custom:nondef (.*)', contract_code)
        if nondef:
            print(f'{contract_path}: {NONDEFINABLE} (nondefinable)')
            return (utils.NONDEFINABLE, nondef.group(1))

        # Tag Negate
        negate = re.search('/// @custom:negate', contract_code)

    # Prepare to fill template command
    params = {}
    params['contract_path'] = contract_path
    params['timeout'] = timeout

    command = COMMAND_TEMPLATE.substitute(params)
    print(command)
    log = subprocess.run(command.split(), capture_output=True, text=True)
    
    if has_error(log.stderr):
        msg = log.stderr
        print(log.stderr, file=sys.stderr)
        if has_source_error(log.stderr):
            msg = 'Use the dot to make a relative import: e.g. "./lib/lib.sol"'
            loggin.error(msg)
        return (ERROR, msg)

    # Timeout
    if (not log.stderr) and (not log.stdout):
        res = WEAK_NEGATIVE
        print(f'{contract_path}: {res} (timeout)')
        return (res, log.stderr)

    if is_timeout_or_unknown(log.stderr):
        res = WEAK_POSITIVE if negate else WEAK_NEGATIVE
        print(f'{contract_path}: {res} (unknown)')
        return (res, log.stderr)

    if has_assertion_warning(log.stderr):
        res = STRONG_POSITIVE if negate else STRONG_NEGATIVE
        print(f'{contract_path}: {res}')
        return (res, log.stderr)

    res = STRONG_NEGATIVE if negate else STRONG_POSITIVE
    print(f'{contract_path}: {res}')
    return (res, log.stderr)


def run_log(id, contract_path, timeout, logs_dir):
    """
    Calls run() and writes the log.
    """
    (outcome, log) = run(contract_path, timeout)
    utils.write_log(logs_dir + id + '.log', log)
    return (id, outcome)


def run_all(contracts_dir, timeout, logs_dir):
    """
    Runs solcmc on all files of a directory.

    Args:
        contracts_dir (str): Contracts directory path.
        timeout (int): Solcmc timeout.

    Returns:
        dict: {p*_v*: (outcome, log)}
    """
    outcomes = {}

    # inputs for run_solcmc_parallel()
    # [(id, contract_path, timeout, logs_dir), ...]
    inputs = []

    for file in os.listdir(contracts_dir):
        if file.endswith('.sol'):     
            id = '_'.join(file.split('_')[-2:]).split('.sol')[0]
            inputs.append((id, contracts_dir + file, timeout, logs_dir))

    with Pool(processes=THREADS) as pool:
        # [(id, outcome), ...]
        results = pool.starmap(run_log, inputs)
        for (id, outcome) in results:
            outcomes[id] = outcome

    return outcomes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contracts',
            '-c',
            help='Contracts dir.',
            required=True
    )
    parser.add_argument(  # build/
            '--output',
            '-o',
            help='Output dir.',
            required=True
    )
    parser.add_argument(
            '--timeout',
            '-t',
            help='Timeout time'
    )
    args = parser.parse_args()

    timeout = args.timeout if args.timeout else DEFAULT_TIMEOUT
    contracts_dir = (
            args.contracts
            if args.contracts[-1] == '/'
            else args.contracts + '/'
            )
    output_dir = args.output if args.output[-1] == '/' else args.output + '/'
    logs_dir = output_dir + 'logs/'

    outcomes = run_all(contracts_dir, timeout, logs_dir)

    out_csv = [utils.OUT_HEADER]

    for id in outcomes.keys():
        p = id.split('_')[0]
        v = id.split('_')[1]
        out_csv.append([p, v, outcomes[id]])

    utils.write_csv(output_dir + 'out.csv', out_csv)
