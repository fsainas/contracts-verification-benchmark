"""
Name: solcmc_contract_builder
Description:
    Generates contracts for solcmc verification using version and
    property files.

Usage:
    python solcmc_contract_builder.py -v <version_dir_or_file>
    -p <property_dir_or_file> [-o <outpu_dir>]
"""

import argparse
import sys
import re
import os

V_PATTERN = r'.*v\d+\.sol$'  # pattern of version file names
P_PATTERN = r".*p\d+\.sol$"  # pattern of property file names


def build_contract(vf_path, pf_path):
    """
    Builds a contract using a version file and a property file.

    Args:
        vf_path (string): Version file path.
        pf_path (string): Property file path.

    Returns:
        tuple: (contract_name, contract_code)
    """

    v_code = ""
    p_code = ""
    contract_name = "".join(vf_path.split('/')[-1].split('_')[0:-1])

    try:
        with open(vf_path, "r") as file:
            v_code = file.read()
    except FileNotFoundError:
        sys.stderr.write(f"\nVersion file not found: {vf_path}")

    try:
        with open(pf_path, "r") as file:
            p_code = file.read()
    except FileNotFoundError:
        sys.stderr.write(f"\nProperty file not found: {pf_path}")

    p_code = "    " + p_code.replace("\n", "\n    ") + '\n\n'   # indentation

    last_brace_index = v_code.rfind('}')
    contract_code = (
            v_code[:last_brace_index] +
            p_code +
            v_code[last_brace_index:]
    )

    return (contract_name, contract_code)


def build_all_contracts(versions, properties):
    """
    Builds all contracts using a version file list and a property file list.

    Args:
        versions (list): A list of tuples [(version_id, file_path), ...].
        properties (list): A list of tuples [(property_id, file_path), ...].

    Returns:
        dict: { filename: contract_code, ...}
    """

    contracts = {}

    for v, vf in versions:
        for p, pf in properties:
            contract_name, code = build_contract(vf,pf)
            filename = contract_name + '_' + p + '_' + v + '.sol'
            contracts[filename] = code

    return contracts


def get_version_list(v_path):
    """
    Generates version list from a directory or file path.

    Args:
        v_path (string): Version directory or file path.

    Returns:
        list: Version list [(version_id, file_path), ...]
    """

    versions = []      # [(v*, path), ...]

    if os.path.isdir(v_path):
        v_dir = v_path if v_path[-1] == '/' else v_path + '/'
        for filename in os.listdir(v_dir):
            if re.match(V_PATTERN, filename):
                v_id = filename.split('_')[-1].split('.sol')[0]    # v*
                path = v_dir + filename
                versions.append((v_id, path))
    else:
        v_id = v_path.split('/')[-1].split('_')[-1].split('.sol')[0]    # v*
        versions = [(v_id, v_path)]

    versions.sort()
    return versions


def get_property_list(p_path):
    """
    Generates property list from a directory or file path.

    Args:
        p_path (string): Property directory or file path.

    Returns:
        list: Property list [(p_id, path), ...]
    """

    properties = []     # [(p*, path), ...]

    if os.path.isdir(p_path):
        p_dir = p_path if p_path[-1] == '/' else p_path + '/'
        for filename in os.listdir(p_dir):
            if re.match(P_PATTERN, filename):
                p_id = filename.split('.sol')[0]    # p*
                path = p_dir + filename
                properties.append((p_id, path))
    else:
        p_id = p_path.split('/')[-1].split('.sol')[0]    # p*
        properties = [(p_id, p_path)]

    properties.sort()
    return properties


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--version',
            '-v',
            help='Version file or dir path.',
            required=True
    )
    parser.add_argument(
            '--property',
            '-p',
            help='Property file or dir path.',
            required=True
    )
    parser.add_argument(
            '--output',
            '-o',
            help='Output directory path.',
    )
    args = parser.parse_args()

    # Check Args
    if args.output:
        if not os.path.isdir(args.output):
            sys.stderr.write("The argument of '--output' must be a directory.\n")
            sys.exit()
        else:
            args.output = args.output if args.output[-1] == '/' else args.output + '/'

    contracts = build_all_contracts(
            get_version_list(args.version),
            get_property_list(args.property)
    )

    for name in contracts.keys():
        if args.output:
            with open(args.output + name, 'w') as contract_file:
                contract_file.write(contracts[name])
        else:
            print(contracts[name])
