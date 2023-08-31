"""
Name: run_certora
Description:
    Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -i <file_or_dir> -o <output_dir>
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


def has_property_error(output, property):
    pattern = rf".*ERROR: [rule] {re.escape(property).upper()}:.*"
    return re.search(pattern, output, re.DOTALL)


def get_contract_name(contract):
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


def get_properties(spec):
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


def run_certora(contract, spec, property):

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
    print(log)

    if has_property_error(log.stdout, property):
        return (STRONG_NEGATIVE, log.stdout)
    else:
        return (STRONG_POSITIVE, log.stdout)


def run_all_certora(contracts_dir, spec):
    outcomes = {}

    properties = get_properties(spec)

    for file in os.listdir(contracts_dir):
        if not os.path.isdir(file):     # lib/ is ignored
            for p in properties:
                id = p.lower() + '_' + file.split('_')[-1].split('.sol')[0]
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
    spec_file = args.spec

    outcomes = run_all_certora(contracts_dir, spec_file)

    for id in outcomes.keys():
        print(id)
        print(outcomes[id][0])
        print(outcomes[id][1])
