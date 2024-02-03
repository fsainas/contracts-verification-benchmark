"""
Script for injecting getters into contracts to be verified with Certora.
"""
from setup.injector import inject_before_last_bracket
from pathlib import Path
import argparse
import glob
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contracts',
            '-c',
            help='Contract file or dir path.',
            required=True)
    parser.add_argument(
            '--getters',
            '-g',
            help='Getters file path.',
            required=True)
    parser.add_argument(
            '--output',
            '-o',
            help='Output directory path.')
    args = parser.parse_args()

    contracts = Path(args.contracts)

    contracts_paths = (
            glob.glob(f'{contracts}/*v*.sol')
            if os.path.isdir(args.contracts)
            else [args.contracts])

    for contract_path in contracts_paths:
        # Save contract lines of code
        contract = []
        with open(contract_path, 'r') as f:
            contract = f.readlines()

        getters = []
        with open(args.getters, 'r') as f:
            getters = f.readlines()

        contract_with_getters = ''.join(l for l in inject_before_last_bracket(contract, getters))

        # Extract file name from contract path
        filename = Path(contract_path).name

        if args.output:
            output = Path(args.output)
            with open(output.joinpath(filename), 'w') as f:
                f.write(contract_with_getters)
        else:
            print(contract_with_getters)
