'''
Utilities to run the toolchain such as common strings and useful functions.
'''

import csv
import logging
import re

OUT_HEADER = ['property', 'version', 'outcome', 'footnote']     # outcome in P,P!,N,N!

WEAK_POSITIVE = 'P'
WEAK_NEGATIVE = 'N'
STRONG_POSITIVE = 'P!'
STRONG_NEGATIVE = 'N!'
NONDEFINABLE = 'ND'
ERROR = 'ERR'


def write_log(path, log):
    with open(path, 'w') as file:
        file.write(log)


def write_csv(path, rows):
    rows = [rows[0]] + sorted(rows[1:])
    with open(path, 'w') as file:
        csv.writer(file).writerows(rows)


def remove_comments(file_content):
    # Remove single-line comments
    file_content = re.sub(r'//.*\n', '', file_content)
    # Remove multi-line comments
    file_content = re.sub(r'/\*(.|\n)*?\*/', '', file_content)
    return file_content


def get_contract_name(contract_path):
    """
    Extracts the contract name from a contract path.

    Args:
        contract (str): Contract file path.

    Returns:
        str: Contract name.
    """
    contract_code = ""

    with open(contract_path, 'r') as contract_file:
        contract_code = contract_file.read()

    contract_code = remove_comments(contract_code)

    matches = re.findall(r'contract\s+([^ ]+)', contract_code)

    if matches:
        # The contract to verify is the last one
        contract_name = matches[-1]
        return contract_name
    else:
        logging.error(f"{contract_path}: Couldn't retrieve contract name.")
        return
