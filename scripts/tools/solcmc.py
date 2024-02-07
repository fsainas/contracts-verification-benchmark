'''
Operates on either a single file or every file within a directory.

Usage:
    python run_solcmc.py -i <file_or_dir> -o <output_dir> [-t <timeout>]
'''

from multiprocessing import Pool
from string import Template
from pathlib import Path
import subprocess
import logging
import utils
from utils import (STRONG_POSITIVE,
                   STRONG_NEGATIVE,
                   WEAK_POSITIVE,
                   WEAK_NEGATIVE,
                   NONDEFINABLE,
                   UNKNOWN,
                   ERROR)
import sys
import re
import os

DEFAULT_TIMEOUT = '10m'
DEFAULT_SOLVER = 'z3'
THREADS = 6

TAG_NONDEF = '/// @custom:nondef'
TAG_NEGATE = '/// @custom:negate'

COMMAND_TEMPLATE = Template(
        'timeout $timeout ' +
        'solc $contract_path ' +
        '--model-checker-engine chc ' +
        '--model-checker-timeout 0 ' +
        '--model-checker-targets assert ' +
        '--model-checker-show-unproved ' +
        '--model-checker-solvers=$solver')


def has_error(output):
    pattern = r'.*Error:.*'
    return re.search(pattern, output, re.DOTALL)


def has_source_error(output):
    pattern = r'.*Error: Source.*'
    return re.search(pattern, output, re.DOTALL)


def has_assertion_violation(output):
    pattern = r'.*Warning: CHC: Assertion violation happens here.*'
    return re.search(pattern, output, re.DOTALL)


def has_weak_assertion_violation(output):
    pattern = r'.*Warning: CHC: Assertion violation might happen here.*'
    return re.search(pattern, output, re.DOTALL)


def warning_solver_not_found(output):
    pattern = r'.*Warning: Solver (.*) was selected for SMTChecker but it was not found.*'
    return re.search(pattern, output, re.DOTALL)


def is_ignoring_timeout(output):
    return 'ignoring option :timeout' in output


def verification_passed(output):
    return 'verification condition(s) proved safe!' in output


def run(contract_path, timeout=DEFAULT_TIMEOUT, solver=DEFAULT_SOLVER):
    '''
    Runs a single solcmc experiment.

    Returns:
        tuple: (outcome, log)
    '''
    # File not found
    if not os.path.isfile(contract_path):
        msg = f'{contract_path} not found.'
        logging.error(msg)
        return ERROR, msg

    with open(contract_path, 'r') as file:
        contract_code = file.read()

    # Process tags
    # Tag Nondefinable
    nondef = re.search(TAG_NONDEF + ' (.*)', contract_code)
    if nondef:
        print(f'{contract_path}: {NONDEFINABLE}')
        return NONDEFINABLE, nondef.group(1)

    # Tag Negate
    negate = re.search(TAG_NEGATE, contract_code)

    # Prepare to fill template command
    params = {}
    params['contract_path'] = contract_path
    params['timeout'] = timeout
    params['solver'] = solver

    command = COMMAND_TEMPLATE.substitute(params)
    #print(command) # substitute with a log that does not go to stdout
    log = subprocess.run(command.split(), capture_output=True, text=True)

    # Invalid time interval
    if 'invalid time' in log.stderr:
        msg = f'Invalid time interval "{timeout}".'
        logging.error(msg)
        return ERROR, msg

    if has_error(log.stderr):
        if has_source_error(log.stderr):
            msg = 'Use the dot to make a relative import: e.g. "./lib/lib.sol"'
        else:
            msg = log.stderr
        print(log.stderr, file=sys.stderr)
        logging.error(msg)
        return ERROR, msg

    solver_not_found = warning_solver_not_found(log.stderr)

    if solver_not_found:
        solver = solver_not_found.group(1)
        msg = f'Solver {solver} was not found. Check installation.'
        logging.error(msg)
        return ERROR, msg
        
    if has_weak_assertion_violation(log.stderr):
        res = WEAK_POSITIVE if negate else WEAK_NEGATIVE
    elif has_assertion_violation(log.stderr):
        res = STRONG_POSITIVE if negate else STRONG_NEGATIVE
    elif verification_passed(log.stderr):
        res = STRONG_NEGATIVE if negate else STRONG_POSITIVE
    elif ((not log.stderr) and (not log.stdout)
        or is_ignoring_timeout(log.stderr)):   # Timeout
        res = UNKNOWN
    else:
        res = ERROR

    print(f'{contract_path}: {res}')
    return res, log.stderr


def run_log(id, contract_path, timeout=DEFAULT_TIMEOUT, logs_dir=None, solver=DEFAULT_SOLVER):
    '''
    Calls run() and writes the log.
    '''
    outcome, log = run(contract_path, timeout, solver)
    if logs_dir:
        utils.write_log(Path(logs_dir).joinpath(id + '.log'), log)
    else:
        print(log)
        print(f'Result: {outcome}')
    return id, outcome


def run_all(contracts_paths, timeout=DEFAULT_TIMEOUT, logs_dir=None, solver=DEFAULT_SOLVER):
    '''
    Runs solcmc on all files of a directory.

    Args:
        contracts_paths (list): Contracts paths.
        timeout (int): Solcmc timeout.

    Returns:
        dict: {key_v*: outcome}
    '''
    outcomes = {}

    # inputs for run_solcmc_parallel()
    # [(id, contract_path, timeout, logs_dir), ...]
    inputs = []

    for contract_path in contracts_paths:
        id = '_'.join(contract_path.split('_')[-2:]).split('.sol')[0]
        inputs.append((id, contract_path, timeout, logs_dir, solver))

    with Pool(processes=THREADS) as pool:
        # [(id, outcome), ...]
        results = pool.starmap(run_log, inputs)
        for (id, outcome) in results:
            outcomes[id] = outcome

    return outcomes
