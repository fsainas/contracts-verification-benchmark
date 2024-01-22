# MERGE TO solcmc.py
"""
Name: runc
Description:
    Run a single solcmc experiment.

Usage:
    python runc.py -c <file_or_dir> -t <timeout> 
"""
import os
import sys
import argparse
import run_solcmc

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contract',
            '-c',
            help='Contract file path.',
            required=True
    )
    parser.add_argument(
            '--timeout',
            '-t',
            help='Timeout time'
    )
    args = parser.parse_args()

    contract = args.contract
    if os.path.isdir(contract):
        print("Contract file expected, but directory was provided: " +
              contract, 
              file=sys.stderr)
        sys.exit(1)
    timeout = args.timeout

    (out, log) = run_solcmc.run(contract, timeout)
    print(log)
    print("Result: " + out) 
