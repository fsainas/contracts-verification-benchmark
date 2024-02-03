"""
Utilities to run the toolchain such as common strings and useful functions.
"""
from pathlib import Path
import logging
import csv
import re
import os

OUT_HEADER = ['property', 'version', 'outcome', 'footnote']     # outcome in P,P!,N,N!

WEAK_POSITIVE = 'P'
WEAK_NEGATIVE = 'N'
STRONG_POSITIVE = 'P!'
STRONG_NEGATIVE = 'N!'
NONDEFINABLE = 'ND'
UNKNOWN = 'UNK'
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
    contract_code = ''

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


def get_files_in_path(input_path, extensions=None):
    path = Path(input_path)
    if path.is_dir():
        # If it's a directory, list all files inside with the specified extensions
        if extensions:
            files = [file for file in path.iterdir()
                     if file.is_file() and file.suffix in extensions]
        else:
            files = [file for file in path.iterdir() if file.is_file()]
    else:
        # If it's a file, use the file itself if it matches the specified extensions
        files = [path] if not extensions or path.suffix in extensions else []

    return files


def find_paths_with_subpath(dir: str, subpath: str):
    """
    Given a subpath finds all files that matches inside a given directory.
    """
    file_paths = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if subpath in os.path.join(root, file):
                file_paths.append(os.path.join(root, file))
    return file_paths


def get_properties(version_path: str, properties_paths: list):
    """
    Determine the properties to verify for a given version based on the provided
    version path and a list of property paths. This function returns a list of
    properties, including generic properties and specific properties if present.

    Args:
        version_path (str): The path to the version.
        properties_paths (list): A list of paths to properties.

    Returns:
        list: The properties to verify for the specified version.

    """

    # Extract base id from base path (e.g. v1)
    version_id = Path(version_path).stem.split('_')[1]

    # Properties associated with the current version
    version_specific_properties_paths = [p for p in properties_paths if f'_{version_id}.' in p]

    # Remove the generic version when there is a specific one
    version_generic_properties_paths = [p for p in properties_paths if '_v' not in p]
    for specific_property_path in version_specific_properties_paths:

        property_id = Path(specific_property_path).stem.split('_')[0]

        version_generic_properties_paths = [p for p in version_generic_properties_paths
                                            if (property_id not in p)]

    return version_specific_properties_paths + version_generic_properties_paths
