import json
from string import Template
from os import listdir
from mdtable_gen import gen_from_csv
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
            print("\n[Error]: README generation:" +
                  fname + " not found.\n" +
                  str(e),
                  file=sys.stderr)
            sys.exit(1)

        res = re.search('/// @custom:version (.*)', content)
        if res:
            versions.append(res.group(1))
        else:
            logging.warning(f'{fname} has no version comment.')
    return versions


def readme_gen(usecase_dir):

    try:
        with open(f'{usecase_dir}/skeleton.json') as f:
            skeleton = json.loads(f.read())
    except json.decoder.JSONDecodeError as e:
        print("\n[Error]: README generation:" +
              " Bad skeleton.json formatting.\n" +
              str(e),
              file=sys.stderr)
        sys.exit(1)

    # Check properties formatting
    if not isinstance(skeleton['properties'], dict): 
        print("\n[Error]: README generation: " +
              "Bad formatting of properties in skeleton.json.\n",
              file=sys.stderr)
        sys.exit(1)

    # Pattern for allowed characters in keys
    key_pattern = re.compile(r'^[a-zA-Z0-9_-]+$')

    # Check each key against the pattern
    for key in skeleton['properties'].keys():
        if not key_pattern.match(key):
            print("\n[Error]: README generation: " +
                  f"Key '{key}' does not match the pattern [a-zA-Z0-9_-]+",
                  file=sys.stderr)
            sys.exit(1)

    try:
        readme = {}
        readme['name'] = skeleton['name']
        readme['specification'] = skeleton['specification']
        readme['properties'] = md_property_list(skeleton['properties'])
        readme['versions'] = md_version_list(get_versions(f'{usecase_dir}/versions/'))
        readme['ground_truth'] = gen_from_csv(f'{usecase_dir}/ground-truth.csv')
    except IndexError:
        print("\n[Error]: README generation:" +
              " Empty line or missing values in ground-truth.csv.\n",
              file=sys.stderr)
        sys.exit(1)

    return PLAIN_README_TEMPLATE.substitute(readme)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--usecase_dir',
                        '-d',
                        help='Usercase directory',
                        required=True)

    args = parser.parse_args()

    print(readme_gen(args.usecase_dir))
