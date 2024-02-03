"""
Generates the plain README.
"""
from report_gen.readme import gen
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--usecase_dir',
                        '-d',
                        help='Usercase directory',
                        required=True)

    args = parser.parse_args()

    print(gen(args.usecase_dir))
