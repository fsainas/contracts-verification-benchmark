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

    Returns:
        dict: { filename: contract_code, ...}
    """

    # Specific properties
    bounded_properties_paths = list(filter(
            lambda x: re.search("p.*_v.*", x),
            properties_paths))
    unbounded_properties_paths = list(
            set(properties_paths) - set(bounded_properties_paths))

    contracts = {}

    for v_path in versions_paths:
        # Extract base id from base path (e.g. v1)
        v_id = v_path.split('/')[-1].split('_')[-1].split('.')[0]

        v_bounded = list(filter(
                lambda x: re.search(f'p.*_{v_id}.*', x), 
                bounded_properties_paths))
        
        v_unbounded = unbounded_properties_paths

        for bp_path in v_bounded:
            p_id = bp_path.split('/')[-1].split('_')[0]     # ../p1_v1.sol -> p1
            # Remove bounded properties from the unbounded variants
            v_unbounded = list(filter(
                    lambda x: not re.search(f'{p_id}', x),
                    v_unbounded
                    ))

        v_properties_paths = v_bounded + v_unbounded

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
            glob.glob(f'{args.properties}/p*.sol')
            if os.path.isdir(args.properties)
            else [args.properties]
    )

    contracts = build_contracts(
            versions_paths,
            properties_paths 
    )
