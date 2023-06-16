import subprocess
import os
import sys
import re
import csv
import argparse

# Default params
default_solcmc_timeout = 1000

# Symbols
timeout_or_unknown = "?"
true_positive = "TP"
true_negative = "TN"
false_positive = "FP"
false_negative = "FN"

# Parsing args
parser = argparse.ArgumentParser()
parser.add_argument('--directory', '-d', help='Directory of the contract')
parser.add_argument('--timeout', '-t', help='Timeout time', default=default_solcmc_timeout)
args = parser.parse_args()

if args.directory is None:
    print("Please provide the directory.")
    sys.exit()

# Paths
dir = args.directory
solcmc_path = str(args.directory) + "/solcmc/"
certora_path = str(args.directory) + "/certora/"
shell_script_name = "run.sh"
input_file = str(args.directory) + "/in.csv"

# Params
solcmc_timeout = args.timeout if args.timeout is not None else default_solcmc_timeout


# Check for assertion warnings in solcmc
def has_assertion_warning(stderr):
    pattern = r".*Warning: CHC: Assertion violation happens here.*"
    return re.search(pattern, stderr, re.DOTALL)


# Check for timeouts or unknown in solcmc
def is_timeout_or_unknown(stderr):
    pattern = r".*Warning: CHC: Assertion violation might happen here.*"
    return re.search(pattern, stderr, re.DOTALL)


# Runs the default solCMC test.
# Returns true if it passes
def solcmc_test(filename, sat):
    command = [solcmc_path + shell_script_name, solcmc_path + filename, str(solcmc_timeout)]
    result = subprocess.run(command, capture_output=True, text=True)
    if (is_timeout_or_unknown(result.stderr)):
        return timeout_or_unknown
    else:
        return calc_result(not has_assertion_warning(result.stderr), sat)


# Runs the default certora test.
# Returns true if it passes
def certora_test(filename):
    return True


def calc_result(obtained, expected):
    if obtained:
        return true_positive if str(expected) == "1" else false_positive
    else:
        return false_negative if str(expected) == "1" else true_negative


def write_header_row(file_path, header):
    with open(file_path, 'w', newline='') as output:
        csv.writer(output).writerow(header)


def append_row(file_path, row):
    with open(file_path, 'a') as output:
        csv.writer(output).writerow(row)


def run_all_tests():
    with open(input_file, 'r') as input:
        csv_reader = csv.reader(input)

        first_line = next(csv_reader)

        write_header_row(solcmc_path + "out.csv", first_line + ["result"])
        write_header_row(certora_path + "out.csv", first_line + ["result"])

        for row in csv_reader:
            p, v, sat = row[0], row[1], row[2]
            pattern = rf".*{re.escape(p)}_{re.escape(v)}.*"

            for filename in os.listdir(solcmc_path):
                if re.match(pattern, filename):
                    solcmc_result = solcmc_test(filename, sat)
                    append_row(solcmc_path + "out.csv", [p, v, sat, solcmc_result])


run_all_tests()
