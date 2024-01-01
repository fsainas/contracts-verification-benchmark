"""
Name: injector
Description:
    Given a list of base files and a list of to-inject files,
    updates all the base files and writes them into a specified dir.

Usage:
    python injector.py -b <base_file_path>
    -i <to_inject_path> [-o <output_dir>]
"""

import argparse
import glob
import os


def inject_code(base_file: str, to_inject_file: str) -> str:
    """
    Injects code of a to-inject file before the last bracket of a base file.

    Returns:
        str: updated_file
    """

    base_code = ""
    to_inject_code = ""

    with open(base_file, "r") as file:
        base_code = file.read()

    with open(to_inject_file, "r") as file:
        to_inject_code = file.read()

    to_inject_code = (   # indentation
            "    " +
            to_inject_code.replace("\n", "\n    ") +
            '\n\n'
    )

    last_brace_index = base_code.rfind('}')
    updated_file = (
            base_code[:last_brace_index] +
            to_inject_code +
            base_code[last_brace_index:]
    )

    return updated_file


def inject_product(base_files: list, to_inject_files: list) -> dict:
    """
    Returns:
        dict: { filename: file_contents, ...}
    """

    updated_files = {}

    for b_path in base_files:

        # Extract file name from base path
        file_name = "".join(b_path.split('/')[-1].split('_')[0:-1])
        file_ext = b_path.split('.')[-1]

        # Extract base id from base path (e.g. v1)
        b_id = b_path.split('/')[-1].split('_')[-1].split('.')[0]

        for i_path in to_inject_files:
            # e.g. p1 for solcmc or getters for certora
            i_id = i_path.split('.')[-2].split('/')[-1].split('_')[0]
            file = inject_code(b_path, i_path)
            filename = file_name + '_' + i_id + '_' + b_id + '.' + file_ext
            updated_files[filename] = file 

    return updated_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--base',
            '-v',
            help='Base file or dir path.',
            required=True
    )
    parser.add_argument(
            '--inject',
            '-p',
            help='To-inject file or dir path.',
            required=True
    )
    parser.add_argument(
            '--output',
            '-o',
            help='Output directory path.',
    )
    args = parser.parse_args()

    args.output = args.output if args.output[-1] == '/' else args.output + '/'

    base_files = (
            glob.glob(f'{args.base}/*v*.sol')
            if os.path.isdir(args.base)
            else [args.base]
    )

    to_inject_files = (
            glob.glob(f'{args.inject}/p*.sol')
            if os.path.isdir(args.inject)
            else [args.inject]
    )

    updated_files = inject_product(
            base_files,
            to_inject_files
    )

    for name in updated_files.keys():
        if args.output:
            with open(args.output + name, 'w') as file:
                file.write(updated_files[name])
        else:
            print(updated_files[name])
