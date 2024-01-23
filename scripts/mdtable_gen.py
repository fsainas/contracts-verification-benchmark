'''
Creates a markdown table from a csv file with this scheme: cols, rows, data.

Usage:
    python mdtable_gen.py --input file.csv
'''

from report_gen.mdtable import gen_from_csv
import argparse
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # cm.csv
    parser.add_argument(
            '--input',
            '-i',
            help='CSV input file',
            required=True
    )
    args = parser.parse_args()

    mdtable = gen_from_csv(args.input)

    sys.stdout.write(mdtable)
