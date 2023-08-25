import subprocess
import os
import sys
import re
import csv
import argparse
import datetime

# Default params
default_solcmc_timeout = 0
default_tool = "all"

# Symbols
timeout_or_unknown = "?"
true_positive = "TP"
true_negative = "TN"
false_positive = "FP"
false_negative = "FN"

# Parsing args
parser = argparse.ArgumentParser()
parser.add_argument('--directory', '-d', help='Directory of the contract')
parser.add_argument('--timeout', '-t', help='Timeout time')
parser.add_argument('--tool', '-T', choices=['solcmc', 'certora', 'all'], help='Verification tool to use', default="all")
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
tool = args.tool if args.tool is not None else default_tool


# Check for assertion warnings in solcmc
def has_assertion_warning(output):
    pattern = r".*Warning: CHC: Assertion violation happens here.*"
    return re.search(pattern, output, re.DOTALL)


# Check for timeouts or unknown in solcmc
def is_timeout_or_unknown(output):
    pattern = r".*Warning: CHC: Assertion violation might happen here.*"
    return re.search(pattern, output, re.DOTALL)

# Check for assertion warnings in certora
def has_property_error(output, p):
    pattern = rf".*ERROR: [rule] {re.escape(p).upper()}:.*"
    return re.search(pattern, output, re.DOTALL)


# Runs the default solCMC test.
# Returns true if it passes
def solcmc_test(filename, sat):
    command = [solcmc_path + shell_script_name, solcmc_path + filename, str(solcmc_timeout)]
    result = subprocess.run(command, capture_output=True, text=True)
    write_log(solcmc_path + "log.txt", result)
    if (is_timeout_or_unknown(result.stderr)):
        return timeout_or_unknown
    else:
        return calc_result(not has_assertion_warning(result.stderr), sat)


# Runs the default certora test.
# Returns true if it passes
def certora_test(base_contract, contract_name, spec_file, p, sat):
    command = [
            certora_path + shell_script_name, 
            certora_path + base_contract, 
            contract_name,
            certora_path + spec_file
            ]
    result = subprocess.run(command, capture_output=True, text=True)
    write_log(certora_path + "log.txt", result)
    return calc_result(not has_property_error(result.stdout, p), sat)


def calc_result(obtained, expected):
    if obtained:
        return true_positive if str(expected) == "1" else false_positive
    else:
        return false_negative if str(expected) == "1" else true_negative


def write_log(log_path, output):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {output}\n"

    with open(log_path, 'a') as log_file:
        log_file.write(log_entry)
        

def write_header_row(file_path, header):
    with open(file_path, 'w', newline='') as output:
        csv.writer(output).writerow(header)


def append_row(file_path, row):
    with open(file_path, 'a') as output:
        csv.writer(output).writerow(row)


def run_all_tests(tool):
    with open(input_file, 'r') as input:
        csv_reader = csv.reader(input)

        first_line = next(csv_reader)

        if tool == "all" or tool == "solcmc":
            write_header_row(solcmc_path + "out.csv", first_line + ["result"])
        if tool == "all" or tool == "certora":
            write_header_row(certora_path + "out.csv", first_line + ["result"])

        for row in csv_reader:
            p, v, sat = row[0], row[1], row[2]

            if tool == "all" or tool == "solcmc":
                solcmc_file_pattern = rf".*{re.escape(p)}_{re.escape(v)}.sol*"
                solcmc_file = ""

                for filename in os.listdir(solcmc_path):
                    if re.match(solcmc_file_pattern, filename):
                        solcmc_file = filename

                if solcmc_file != "":
                    result = solcmc_test(solcmc_file, sat)
                    append_row(solcmc_path + "out.csv", [p, v, sat, result])

            if tool == "all" or tool == "certora":
                base_contract_pattern = rf".*{re.escape(v)}.sol.*"
                spec_file_pattern = rf".*{re.escape(p)}.spec.*"
                base_contract = ""
                spec_file = ""

                for filename in os.listdir(certora_path):
                    if re.match(base_contract_pattern, filename):
                        base_contract = filename
                    if re.match(spec_file_pattern, filename):
                        spec_file = filename

                if base_contract != "" and spec_file != "":
                    contract_name = base_contract.split("_")[0]     # "Name_v?.sol".split("_")[0]

                    result = certora_test(base_contract, contract_name, spec_file, p, sat)
                    append_row(certora_path + "out.csv", [p, v, sat, result])


run_all_tests(tool)
