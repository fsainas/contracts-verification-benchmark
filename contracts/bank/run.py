import subprocess
import re
import os
import csv

solcmc_path = "./solCMC/"
certora_path = "./certora/"
shell_script_name = "run.sh"
input_file = "in.csv"


# Check for assertion warnings in solcmc output
def has_assertion_warning(stderr):
    pattern = r".*Warning: CHC: Assertion.*"
    return re.search(pattern, stderr, re.DOTALL)


# Runs the default solCMC test.
# Returns true if it passes
def solcmc_test(filename):
    command = [solcmc_path + shell_script_name, solcmc_path + filename]
    result = subprocess.run(command, capture_output=True, text=True)
    return not has_assertion_warning(result.stderr)


# Runs the default certora test.
# Returns true if it passes
def certora_test(filename):
    return True


def calc_result(obtained, expected):
    if obtained:
        return "TP" if expected == "1" else "FP"
    else:
        return "FN" if expected == "1" else "TN"


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
                    solcmc_result = solcmc_test(filename)
                    result = calc_result(solcmc_result, sat)
                    append_row(solcmc_path + "out.csv", [p, v, sat, result])


run_all_tests()
