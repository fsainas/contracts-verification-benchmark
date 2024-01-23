'''
Generates solcmc contracts from versions and properties files.

Usage:
    python builder.py -b <versions_path>
    -i <properties_path> [-o <output_dir>]
'''

from setup.instrumentation import instrument_contracts
import argparse
import glob
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--versions',
            '-v',
            help='Version file or dir path.',
            required=True
    )
    parser.add_argument(
            '--properties',
            '-p',
            help='Property file or dir path.',
            required=True
    )
    parser.add_argument(
            '--output',
            '-o',
            help='Output directory path.',
    )
    args = parser.parse_args()

    if args.output:
        args.output = args.output if args.output[-1] == '/' else args.output + '/'

    args.versions = (
            args.versions
            if args.versions[-1] != '/'
            else args.versions[:-1]
            )

    args.properties = (
            args.properties
            if args.properties[-1] != '/'
            else args.properties[:-1]
            )

    versions_paths = (
            glob.glob(f'{args.versions}/*v*.sol')
            if os.path.isdir(args.versions)
            else [args.versions]
    )

    properties_paths = (
            glob.glob(f'{args.properties}/*.sol')
            if os.path.isdir(args.properties)
            else [args.properties]
    )

    contracts = instrument_contracts(
            versions_paths,
            properties_paths
    )

    for name in contracts.keys():
        if args.output:
            with open(args.output + name, 'w') as file:
                file.write(contracts[name])
        else:
            print(contracts[name])
