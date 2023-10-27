"""
Name: run_certora
Description:
    Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -i <file_or_dir> -s <spec_file> -o <output_dir>
"""

from string import Template
import subprocess
import glob
import os
import sys
import re
import csv
import argparse
import datetime

COMMAND_TEMPLATE = Template(
"""certoraRun $contract:$name \
--verify $name:$spec
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

# Check if there is an error in the output (Dep)
def has_property_error(output, property):
    pattern = rf".*ERROR: \[rule\] {re.escape(property).upper()}.*"
    return re.search(pattern, output, re.DOTALL)


def no_errors_found(output):
    pattern = rf".*No errors found by Prover!.*"
    return re.search(pattern, output, re.DOTALL)


def has_critical_error(output):
    pattern = rf".*CRITICAL.*"
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
        contract_name = matches[0]
        return contract_name
    else:
        sys.stderr.write(
                '[Error]:' +
                f'{contract}:' +
                f"Couldn't retrieve contract name.\n"
        )
        return


def run_certora(contract, spec_path):
    """
    Runs a single certora experiment.

    Args:
        contract (str): Contract file path.
        spec_path (str): CVL spec file path.

    Returns:
        tuple: (outcome, log)
    """

    contract_name = get_contract_name(contract)

    if not contract_name:
        return

    params = {}
    params['contract'] = contract 
    params['name'] = contract_name
    params['spec'] = spec_path
    #params['property'] = property

    command = COMMAND_TEMPLATE.substitute(params)
    print(command)
    log = subprocess.run(command.split(), capture_output=True, text=True)

    if log.stderr:
        print(log.stderr, file=sys.stderr)

    if has_critical_error(log.stdout):
        print(log.stdout, file=sys.stderr)
        sys.exit(1)

    if no_errors_found(log.stdout):
        return (STRONG_POSITIVE, log.stdout+"\n"+log.stderr)
    else:
        return (STRONG_NEGATIVE, log.stdout+"\n"+log.stderr)


def get_properties(spec_path):
    """
    Retrieves the list of properties defined in CVL spec files.

    Args:
        spec (str): CVL specs file or dir path.

    Returns:
        list: The list of property names.
    """
    return (
            glob.glob(f'{spec_path}/p*.spec')
            if os.path.isdir(spec_path)
            else [spec_path]
    )



def run_all_certora(contracts_dir, spec_path):
    """
    Runs certora on all files of a directory.

    Args:
        contracts_dir (str): Contracts directory path.
        spec (str): CVL spec dir path.

    Returns:
        dict: {p*_v*: (outcome, log)}
    """
    outcomes = {}

    specs = get_properties(spec_path)   # list of paths

    # Specific properties
    bounded_properties_paths = list(filter(
            lambda x: re.search("p.*_v.*", x),
            specs))
    unbounded_properties_paths = list(
            set(specs) - set(bounded_properties_paths))


    for v_path in os.listdir(contracts_dir):
        if not os.path.isdir(contracts_dir + v_path):     # lib/ is ignored

            # Extract base id from base path (e.g. v1)
            v_id = v_path.split('/')[-1].split('_')[-1].split('.')[0]

            v_bounded = list(filter(
                    lambda x: re.search(f'p.*_{v_id}.*', x), 
                    bounded_properties_paths))

            
            v_unbounded = unbounded_properties_paths

            for bp_path in v_bounded:
                p_id = bp_path.split('/')[-1].split('_')[0]     # ../p1_v1.sol -> p1
                # Remove bounded properties from the unbounded variants
                v_unbounded = list(filter(
                        lambda x: not re.search(f'{p_id}', x),
                        v_unbounded
                        ))

            v_properties_paths = v_bounded + v_unbounded

            for s_path in v_properties_paths:
                id = (  # e.g. p1_v1
                        s_path.split('.')[-2].split('/')[-1].split('_')[0] + 
                        '_' + 
                        v_path.split('_')[-1].split('.sol')[0]
                )
                outcomes[id] = run_certora(contracts_dir + v_path, s_path)

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
            help='CVL Specification dir or file.',
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
    spec_path = args.spec if args.spec[-1] == '/' else args.spec + '/'

    outcomes = run_all_certora(contracts_dir, spec_path)

    out_csv = [OUT_HEADER] 
    for id in outcomes.keys():
        out_csv.append([id.split('_')[0], id.split('_')[1], outcomes[id][0]])
        write_log(logs_dir + id + '.log', outcomes[id][1])
    write_csv(output_dir + 'out.csv', out_csv)
