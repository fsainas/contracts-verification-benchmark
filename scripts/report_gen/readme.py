"""
Generates the plain README.
"""

import json
from string import Template
from os import listdir
import mdtable_gen
import re
import sys
import logging
import argparse

PLAIN_README_TEMPLATE = Template(
'''# $name
## Specification
$specification

## Properties
$properties

## Versions
$versions

## Ground truth
$ground_truth'''
)


def md_property_list(properties: dict) -> str:
    """
    Generates the markdown list of properties.

    Args:
        properties (dict): {id: description}
    """
    return '\n'.join(
        f'- **{id}**: {properties[id]}' for id in sorted(properties.keys())
    )


def md_version_list(versions):
    return '\n'.join(
        f'- **v{i+1}**: {p}' for i, p in enumerate(versions)
    )


def version_files(versions_dir):
    return sorted(
        f for f in listdir(versions_dir) if f.endswith('.sol')
    )


def get_versions(versions_dir):
    # could use `solc --devdoc -o . {fname}`
    # but it creates a file for each contract which is harder to parse.
    versions = []
    for fname in version_files(versions_dir):
        try:
            with open(versions_dir + fname) as f:
                content = f.read()
        except FileNotFoundError as e:
            logging.error(f'README generation: {fname} not found.\n{e}')
            sys.exit(1)

        res = re.search('/// @custom:version (.*)', content)
        if res:
            versions.append(res.group(1))
        else:
            logging.warning(f'{fname} has no version comment.')

    return versions


def gen(usecase_dir):

    try:
        with open(f'{usecase_dir}/skeleton.json') as f:
            skeleton = json.loads(f.read())
    except json.decoder.JSONDecodeError as e:
        logging.error(f'README generation: Bad skeleton.json formatting.\n{e}')
        sys.exit(1)

    # Check properties formatting
    if not isinstance(skeleton['properties'], dict):
        logging.error('README generation: Bad formatting of properties in skeleton.json.')
        sys.exit(1)

    # Pattern for allowed characters in property ids
    id_pattern = re.compile(r'^[a-zA-Z0-9-]+$')
    # Check each key against the pattern
    for id in skeleton['properties'].keys():
        if not id_pattern.match(id):
            logging.error(f'README generation: Invalid characters in property ID "{id}".'
                          ' Only alphanumeric characters and \'-\' are allowed.')
            sys.exit(1)

    # Allow specification in a separate file (file:filename.md)
    specification = ''
    if skeleton['specification'].startswith('file:'):
        spec_file_name = skeleton['specification'][len('file:'):]

        try:
            with open(f'{usecase_dir}/{spec_file_name}') as f:
                specification = f.read()
        except FileNotFoundError as e:
            logging.error(f'README generation:\n{e}')
            sys.exit(1)
    else:
        specification = skeleton['specification']

    readme = {}
    readme['name'] = skeleton['name']
    readme['specification'] = specification
    readme['properties'] = md_property_list(skeleton['properties'])
    readme['versions'] = md_version_list(get_versions(f'{usecase_dir}/versions/'))
    readme['ground_truth'] = mdtable_gen.gen_from_csv(f'{usecase_dir}/ground-truth.csv')

    return PLAIN_README_TEMPLATE.substitute(readme)
