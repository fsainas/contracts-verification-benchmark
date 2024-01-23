"""
Name: builder
Description:
    Generates contracts from versions and properties files.

Usage:
    python builder.py -b <versions_path>
    -i <properties_path> [-o <output_dir>]
"""

import injector 
import re
import argparse
import glob
import os


def build_contracts(versions_paths: list, properties_paths: list) -> dict:
    """
    Builds contracts to verify from versions and properties.
    They will go to build/contracts.

    Returns:
        dict: { filename: contract_code, ...}
    """

    # Properties associated with a version
    bound_properties_paths = list(filter(
            lambda x: re.search(".*_v.*", x),
            properties_paths))
    unbound_properties_paths = list(
            set(properties_paths) - set(bound_properties_paths))

    contracts = {}

    for v_path in versions_paths:
        # Extract base id from base path (e.g. v1)
        v_id = v_path.split('/')[-1].split('_')[-1].split('.')[0]

        # Properties associated with the current version v
        v_bound_properties_paths = list(filter(
                lambda x: re.search(f'.*_{v_id}.*', x), 
                bound_properties_paths))

        v_unbound_properties_paths = unbound_properties_paths

        # Remove bound properties from the unbound variants       
        for bp_path in v_bound_properties_paths:
            p_id = bp_path.split('/')[-1].split('_')[0]     # ../p1_v1.sol -> p1

            v_unbound_properties_paths = list(filter(
                    lambda x: not re.search(f'{p_id}', x),
                    v_unbound_properties_paths
                    ))

        v_properties_paths = v_bound_properties_paths + v_unbound_properties_paths

        contracts.update(injector.inject_product([v_path], v_properties_paths))

    return contracts


if __name__ == "__main__":
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

    args.output = args.output if args.output[-1] == '/' else args.output + '/'

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

    contracts = build_contracts(
            versions_paths,
            properties_paths 
    )

    for name in contracts.keys():
        if args.output:
            with open(args.output + name, 'w') as file:
                file.write(contracts[name])
        else:
            print(contracts[name])
