"""
Name: run_certora
Description:
    Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -i <file_or_dir> -s <spec_file> -o <output_dir>
"""

from string import Template
import subprocess
import os
import sys
import re
import csv
import argparse
import datetime

COMMAND_TEMPLATE = Template(
"""certoraRun $contract:$name \
--verify $name:$spec \
--rule $property
"""
)

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


def has_property_error(output, property):
    pattern = rf".*ERROR: \[rule\] {re.escape(property).upper()}.*"
    return re.search(pattern, output, re.DOTALL)


def get_contract_name(contract):
    """
    Extracts the contract name from a contract path.

    Args:
        contract (str): Contract file path.

    Returns:
        str: Contract name.
    """
    contract_code = ""

    with open(contract, 'r') as contract_file:
        contract_code = contract_file.read()

    matches = re.findall(r'contract\s+([^ ]+)', contract_code)

    if matches:
        # The contract to verify is the last one
        contract_name = matches[-1]
        return contract_name
    else:
        sys.stderr.write(
                '[Error]:' +
                f'{contract}:' +
                f"Couldn't retrieve contract name.\n"
        )
        return


def run_certora(contract, spec, property):
    """
    Runs a single certora experiment.

    Args:
        contract (str): Contract file path.
        spec (str): CVL spec file path.
        property (str): Rule to verify.

    Returns:
        tuple: (outcome, log)
    """

    contract_name = get_contract_name(contract)

    if not contract_name:
        return

    params = {}
    params['contract'] = contract 
    params['name'] = contract_name
    params['spec'] = spec
    params['property'] = property

    command = COMMAND_TEMPLATE.substitute(params)
    log = subprocess.run(command.split(), capture_output=True, text=True)

    if has_property_error(log.stdout, property):
        return (STRONG_NEGATIVE, log.stdout)
    else:
        return (STRONG_POSITIVE, log.stdout)


def get_properties(spec):
    """
    Retrieves the list of properties defined in a CVL spec file.

    Args:
        spec (str): CVL spec file path.

    Returns:
        list: The list of property names.
    """
    spec_code = ""

    with open(spec, 'r') as spec_file:
        spec_code = spec_file.read()

    matches = re.findall(r'rule\s+([^ ]+)', spec_code)

    if matches:
        return [ match.split()[-1] for match in matches ] 
    else:
        sys.stderr.write(
                '[Error]:' +
                f'{spec}:' +
                f"Couldn't retrieve properties from spec file.\n"
        )
        return


def run_all_certora(contracts_dir, spec):
    """
    Runs certora on all files of a directory.

    Args:
        contracts_dir (str): Contracts directory path.
        spec (str): CVL spec file path.

    Returns:
        dict: {p*_v*: (outcome, log)}
    """
    outcomes = {}

    properties = get_properties(spec)

    for file in os.listdir(contracts_dir):
        if not os.path.isdir(file):     # lib/ is ignored
            for p in properties:
                id = p.lower() + '_' + file.split('_')[-1].split('.sol')[0]  # e.g. p1_v1
                outcomes[id] = run_certora(contracts_dir + file, spec, p)

    return outcomes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--input', 
            '-i', 
            help='File or directory with contracts.',
            required=True
            )
    parser.add_argument(
            '--spec', 
            '-s', 
            help='CVL Specification file.',
            required=True
            )
    parser.add_argument(  # build/
            '--output',
            '-o',
            help='Directory to write output.',
            #required=True
    )
    args = parser.parse_args()

    contracts_dir = args.input if args.input[-1] == '/' else args.input + '/'
    output_dir = args.output if args.output[-1] == '/' else args.output + '/'
    logs_dir = output_dir + 'logs/'
    spec_file = args.spec

    outcomes = run_all_certora(contracts_dir, spec_file)

    out_csv = [OUT_HEADER] 
    for id in outcomes.keys():
        out_csv.append([id.split('_')[0], id.split('_')[1], outcomes[id][0]])
        write_log(logs_dir + id + '.log', outcomes[id][1])
    write_csv(output_dir + 'out.csv', out_csv)
