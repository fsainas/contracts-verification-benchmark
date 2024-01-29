'''
Operates on either a single file or every file within a directory.

Usage:
    python run_solcmc.py -i <file_or_dir> -o <output_dir> [-t <timeout>]
'''

from tools.solcmc import run_all
import argparse
import glob
import utils
import os

DEFAULT_TIMEOUT = '10m'
DEFAULT_SOLVER = 'z3'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contracts',
            '-c',
            help='Contracts dir or contract file.',
            required=True
    )
    parser.add_argument(  # build/
            '--output',
            '-o',
            help='Output directory.'
    )
    parser.add_argument(
            '--timeout',
            '-t',
            help='Timeout time.'
    )

    parser.add_argument(
            '--solver',
            '-s',
            help='Model checker: {z3, eld}'
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

    timeout = args.timeout if args.timeout else DEFAULT_TIMEOUT
    solver = args.solver if args.solver else DEFAULT_SOLVER

    if args.output:
        output_dir = args.output if args.output[-1] == '/' else args.output + '/'
        logs_dir = output_dir + 'logs/'

        outcomes = run_all(contracts_paths, timeout, logs_dir, solver)

        out_csv = [utils.OUT_HEADER]
        for id in outcomes.keys():
            p = id.split('_')[0]
            v = id.split('_')[1]
            out_csv.append([p, v, outcomes[id]])

        utils.write_csv(output_dir + 'out.csv', out_csv)
    else:
        run_all(contracts_paths, timeout, solver=solver)
