'''
Collection of function to inject code.

Usage:
    python injector.py -b <base_file_path> -i <to_inject_path> [-o <output_dir>]
'''

from setup.injector import inject_product
import argparse
import glob
import os


if __name__ == '__main__':
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
