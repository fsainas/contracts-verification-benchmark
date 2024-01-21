# MERGE TO certora.py
"""
Name: runc
Description:
    Run a single certora experiment.

Usage:
    python runc.py -c <file_or_dir> -s <spec_file> 
"""
import os
import argparse
import run_certora

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--contract',
            '-c',
            help='Contract to verify',
            required=True
            )
    parser.add_argument(
            '--specs',
            '-s',
            help='CVL Specification dir or file.',
            required=True
            )
    args = parser.parse_args()

    contract = args.contract
    if os.path.isdir(contract):
        print("Contract file expected, but directory was provided: " +
              contract, 
              file=sys.stderr)
    spec_path = args.specs

    (out, log) = run_certora.run(contract, spec_path)
    print(log)
    print("Result: " + out) 
