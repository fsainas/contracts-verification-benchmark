'''
Operates on either a single file or every file within a directory.

Usage:
    python run_certora.py -c <file_or_dir> -s <spec_file> -o <output_dir>
'''

from tools.certora import run_all
import argparse
import utils
import glob
import os

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
