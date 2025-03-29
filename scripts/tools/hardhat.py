#!/usr/bin/python3
'''
In order to use this script you need to set up a hardhat project (JavaScript) 
according to the official guide: https://hardhat.org/hardhat-runner/docs/getting-started

It operates on a directory containing a folder with the hardhat PoC.

Usage:
    ./hardhat.py <path_to_hardhat_project> <path_to_contract_directory>

The script gives an output containing the results of the executed test.
'''
import argparse
import os
import shutil
import subprocess
import sys

#Validate the given directories
def check_dir_errors(hardhat_directory, contract_directory, contract_test_files):
    if not os.path.isdir(hardhat_directory):
        print(f"Error: The directory {hardhat_directory} does not exist.")
        sys.exit(1)
    elif not os.path.isdir(contract_directory):
        print(f"Error: The directory {contract_directory} does not exist.")
        sys.exit(1)
    elif len(os.listdir(os.path.join(hardhat_directory, 'contracts'))) != 0:
        print(f"Error: The directory {hardhat_directory}contracts is not empty.")
        sys.exit(1)
    elif len(os.listdir(os.path.join(hardhat_directory, 'test'))) != 0:
        print(f"Error: The directory {hardhat_directory}test is not empty.")
        sys.exit(1)

    config_file = os.path.join(hardhat_directory, 'hardhat.config.js')
    if not os.path.isfile(config_file):
        print(f"Error: The directory {hardhat_directory} does not appear to be a Hardhat project (missing {config_file}).")
        sys.exit(1)
    
    if not os.path.isdir(contract_test_files):
        print(f"Error: The directory {contract_test_files} does not exist.")
        sys.exit(1)

def copy_files(src_dir, dest_dir, file_extension):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for filename in os.listdir(src_dir):
        if filename.endswith(file_extension):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            print(f"Copying {src_file} to {dest_file}...")
            shutil.copy(src_file, dest_file)

def clear_copied_files():
    for dir_to_clear in ["contracts", "test"]:
        for filename in os.listdir(dir_to_clear):
            file_path = os.path.join(dir_to_clear, filename)
            if os.path.isfile(file_path):
                print(f"Removing {file_path}...")
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

def run_hardhat_tests(hardhat_directory, contract_directory):
    
    contract_test_files = os.path.join(contract_directory, 'hardhat')

    check_dir_errors(hardhat_directory, contract_directory, contract_test_files)
    
    copy_files(contract_test_files, os.path.join(hardhat_directory, 'contracts'), '.sol')
    copy_files(contract_test_files, os.path.join(hardhat_directory, 'test'), '.js')

    os.chdir(hardhat_directory)
    env = os.environ.copy()
    env['FORCE_COLOR'] = 'true'
    
    try:
        print(f"Running Hardhat tests in {hardhat_directory}...")
        result = subprocess.run(
            ["npx", "hardhat", "test"], 
            check=True, 
            capture_output=True, 
            text=True,
            env=env
        )
        print("Test Output:\n", result.stdout)
        if result.stderr:
            print("Test Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Error running Hardhat tests:")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")

    clear_copied_files()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python hardhat_test.py <path_to_hardhat_project> <path_to_contract_directory>")
        sys.exit(1)
    
    hardhat_directory = sys.argv[1]
    contract_directory = sys.argv[2]
    
    run_hardhat_tests(hardhat_directory, contract_directory)
