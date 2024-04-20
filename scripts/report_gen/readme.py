"""
Generates the plain README.
"""

import json
from string import Template
from os import listdir
from pathlib import Path
from typing import List
import re
import sys
import logging

from report_gen import mdtable

# Templates
CLASSIC_TEMPLATE = Template(
'''# $name
$credit
## Specification
$specification

## Properties
$properties

## Versions
$versions

## Ground truth
$ground_truth'''
)

REGRESSION_TEMPLATE = Template(
'''# $name
$credit
## Specification
$specification

## Properties
$properties

## Ground truth
$ground_truth'''
)

# Allowed characters for property ids
ALLOWED_ID_CHARS = r'^[a-zA-Z0-9-]+$'

def md_property_list(properties: dict) -> str:
    """
    Generates the markdown list of properties.

    Args:
        properties (dict): {id: description}
    """
    return '\n'.join(
        f'- **{id}**: {properties[id]}' for id in sorted(properties.keys())
    )


def md_version_list(versions: List[str]) -> str:
    """ 
    Generate a markdown list of versions. 

    Args:
        versiosn (list): list of version descriptions.
    """
    return '\n'.join(
        f'- **v{i+1}**: {v}' for i, v in enumerate(versions)
    )


def get_versions_file_paths(versions_dir: Path) -> List[Path]:
    """ Get versions file paths from the versions directory path """
    return sorted(
        Path(f) for f in listdir(versions_dir) if f.endswith('.sol')
    )


def get_versions_descriptions(versions_dir: Path) -> List[str]:
    """ Get versions descriptions from versions directory. """
    # could use `solc --devdoc -o . {fname}`
    # but it creates a file for each contract which is harder to parse.
    versions = []
    for v_path in get_versions_file_paths(versions_dir):
        try:
            with open(versions_dir / v_path, 'r', encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError as e:
            msg = f"README generation: {v_path} not found.\n{e}"
            logging.error(msg)
            sys.exit(1)

        res = re.search('/// @custom:version (.*)', content)
        if res:
            versions.append(res.group(1))
        else:
            msg = f"{v_path} has no version comment."
            logging.warning(msg)

    return versions


def gen(usecase_dir: Path) -> str:
    """ Generate plain README for the the usecase. """

    skeleton_path = usecase_dir / "skeleton.json"
    ground_truth_path = usecase_dir / "ground-truth.csv"
    versions_path = usecase_dir / "versions/"

    try:
        with open(skeleton_path, 'r', encoding="utf-8") as f:
            skeleton = json.loads(f.read())
    except json.decoder.JSONDecodeError as e:
        msg = f"README generation: Bad skeleton.json formatting.\n{e}"
        logging.error(msg)
        sys.exit(1)

    # Check properties formatting
    if not isinstance(skeleton['properties'], dict):
        msg = "README generation: Bad formatting of properties in skeleton.json."
        logging.error(msg)
        sys.exit(1)

    # Pattern for allowed characters in property ids
    id_pattern = re.compile(ALLOWED_ID_CHARS)

    # Check each key against the pattern
    for p in skeleton['properties'].keys():
        if not id_pattern.match(p):
            msg = (
                f'README generation: Invalid characters in property ID "{p}".'
                " Only alphanumeric characters and '-' are allowed.")
            logging.error(msg)
            sys.exit(1)

    # Allow specification in a separate file (file:filename.md)
    if skeleton['specification'].startswith('file:'):

        # Get file name
        spec_file_name = skeleton['specification'][len('file:'):]

        try:
            with open(usecase_dir / spec_file_name, 'r', encoding="utf-8") as f:
                specification = f.read()

        except FileNotFoundError as e:
            msg = f"README generation:\n{e}"
            logging.error(msg)
            sys.exit(1)

    else:
        specification = skeleton['specification']

    # Allow credits in a separate file (file:filename.md)
    if 'credits' in skeleton:
        if skeleton['credits'].startswith('file:'):
            credits_file_name = skeleton['credits'][len('file:'):]

            try:
                with open(usecase_dir / credits_file_name, 'r', encoding="utf-8") as f:
                    credit = f.read()

            except FileNotFoundError as e:
                msg = f"README generation:\n{e}"
                logging.error(msg)
                sys.exit(1)

        else:
            credit = skeleton['credits']

    else:
        credit = ''

    versions = (md_version_list(get_versions_descriptions(versions_path))
    if versions_path.exists() else None)

    readme = {
        "name": skeleton['name'],
        "credit": credit,
        "specification": specification,
        "properties": md_property_list(skeleton['properties']),
        "versions": versions,
        "ground_truth": mdtable.gen_from_csv(ground_truth_path)
    }

    template = CLASSIC_TEMPLATE if versions else REGRESSION_TEMPLATE

    return template.substitute(readme)
