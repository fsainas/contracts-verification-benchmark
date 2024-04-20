"""
Generates the plain README.
"""
import argparse
from pathlib import Path
from report_gen.readme import gen

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--usecase_dir',
                        '-d',
                        help='Usercase directory',
                        required=True)

    args = parser.parse_args()

    print(gen(Path(args.usecase_dir)))
