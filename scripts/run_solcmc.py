"""
Name: run_solcmc
Description:
    Runs on a file or every file inside a directory.

Usage:
    python run_solcmc.py -i <file_or_dir> -o <output_dir> -t <timeout>
"""

import subprocess
from string import Template
import argparse
import csv
import re
import os

COMMAND_TEMPLATE = Template(
"""solc $c_path \
--model-checker-engine chc \
--model-checker-timeout $timeout \
--model-checker-targets assert \
--model-checker-show-unproved \
"""
)

DEFAULT_TIMEOUT = 0

OUT_HEADER = ['property','version','outcome']     # outcome in P,P!,N,N!

WEAK_POSITIVE = "P"
WEAK_NEGATIVE = "N"
STRONG_POSITIVE = "P!"
STRONG_NEGATIVE = "N!"


def write_log(path, log):
    with open(path, 'w') as file:
        file.write(log)


def write_csv(path, rows):
    rows = [rows[0]] + sorted(rows[1:])
    with open(path, 'w') as file:
        csv.writer(file).writerows(rows)


def has_assertion_warning(output):
    pattern = r".*Warning: CHC: Assertion violation happens here.*"
    return re.search(pattern, output, re.DOTALL)


def is_timeout_or_unknown(output):
    pattern = r".*Warning: CHC: Assertion violation might happen here.*"
    return re.search(pattern, output, re.DOTALL)


def run_solcmc(c_path, timeout):
    """
    Runs a single solcmc experiment.

    Args:
        c_path (string): Contract file path.
        timeout (int): Experiment timeout.

    Returns:
        tuple: (outcome, log)
    """
    params = {}
    params['c_path'] = c_path
    params['timeout'] = timeout
    command = COMMAND_TEMPLATE.substitute(params)
    log = subprocess.run(command.split(), capture_output=True, text=True)
    if is_timeout_or_unknown(log.stderr):
        return (WEAK_NEGATIVE, log.stderr)
    elif has_assertion_warning(log.stderr):
        return (STRONG_NEGATIVE, log.stderr)
    else:
        return (STRONG_POSITIVE, log.stderr)


def run_all_solcmc(contracts_dir, timeout):
    """
    Runs solcmc on all files of a directory.

    Args:
        contracts_dir (string): Contracts directory path.
        timeout (int): Solcmc timeout.

    Returns:
        dict: {p*_v*: (outcome, log)}
    """
    outcomes = {}

    for file in os.listdir(contracts_dir):
        if not os.path.isdir(file):     # lib/ is ignored
            id = '_'.join(file.split('_')[-2:]).split('.sol')[0]
            outcomes[id] = run_solcmc(contracts_dir + file, timeout)

    return outcomes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--input',
            '-i',
            help='File or directory with contracts.',
            required=True
    )
    parser.add_argument(  # build/
            '--output',
            '-o',
            help='Directory to write output.',
            required=True
    )
    parser.add_argument(
            '--timeout',
            '-t',
            help='Timeout time'
    )
    args = parser.parse_args()

    timeout = args.timeout if args.timeout else DEFAULT_TIMEOUT
    contracts_dir = args.input if args.input[-1] == '/' else args.input + '/'
    output_dir = args.output if args.output[-1] == '/' else args.output + '/'
    logs_dir = output_dir + 'logs/'

    outcomes = run_all_solcmc(contracts_dir, timeout)

    out_csv = [OUT_HEADER] 
    for id in outcomes.keys():
        out_csv.append([id.split('_')[0], id.split('_')[1], outcomes[id][0]])
        write_log(logs_dir + id + '.log', outcomes[id][1])
    write_csv(output_dir + 'out.csv', out_csv)
