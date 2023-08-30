"""
Name: contract_builder
Description:
    Generates contracts from base contracts and to-inject files.

Usage:
    python contract_builder.py -b <base_contract_path>
    -i <to_inject_path> [-o <output_dir>]
"""

import argparse
import glob
import os


def inject_code(base_contract: str, to_inject_file: str) -> str:
    """
    Injects code from a to-inject file into a base contract.

    Returns:
        str: contract_code
    """

    base_code = ""
    to_inject_code = ""

    with open(base_contract, "r") as file:
        base_code = file.read()

    with open(to_inject_file, "r") as file:
        to_inject_code = file.read()

    to_inject_code = (   # indentation
            "    " +
            to_inject_code.replace("\n", "\n    ") +
            '\n\n'
    )

    last_brace_index = base_code.rfind('}')
    contract_code = (
            base_code[:last_brace_index] +
            to_inject_code +
            base_code[last_brace_index:]
    )

    return contract_code


def build_contracts(base_contracts: list, to_inject_files: list) -> dict:
    """
    Builds contracts from a base contract list and a to-inject file list.

    Returns:
        dict: { filename: contract_code, ...}
    """

    contracts = {}

    for b_path in base_contracts:

        # Extract contract name from base path
        contract_name = "".join(b_path.split('/')[-1].split('_')[0:-1])

        # Extract base id from base path (e.g. v1)
        b_id = b_path.split('/')[-1].split('_')[-1].split('.sol')[0]

        for i_path in to_inject_files:
            # e.g. p1 for solcmc or getters for certora
            i_id = i_path.split('/')[-1].split('.sol')[0]
            contract = inject_code(b_path, i_path)
            filename = contract_name + '_' + i_id + '_' + b_id + '.sol'
            contracts[filename] = contract

    return contracts


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--base',
            '-v',
            help='Version file or dir path.',
            required=True
    )
    parser.add_argument(
            '--inject',
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

    args.output = args.output if args.output[-1] == '/' else args.output + '/'

    base_contracts = (
            glob.glob(f'{args.base}/*v*.sol')
            if os.path.isdir(args.base)
            else [args.base]
    )

    to_inject_files = (
            glob.glob(f'{args.inject}/p*.sol')
            if os.path.isdir(args.inject)
            else [args.inject]
    )

    contracts = build_contracts(
            base_contracts,
            to_inject_files
    )

    for name in contracts.keys():
        if args.output:
            with open(args.output + name, 'w') as contract_file:
                contract_file.write(contracts[name])
        else:
            print(contracts[name])
