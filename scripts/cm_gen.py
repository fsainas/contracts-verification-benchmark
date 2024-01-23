from report_gen.cm import gen
import argparse
import csv
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--ground-truth',
            '-g',
            help='CSV ground-truth file.',
            required=True
    )
    parser.add_argument(
            '--results',
            '-r',
            help='CSV file with results.',
            required=True
    )
    parser.add_argument(
            '--properties',
            '-p',
            help='Properties directory, to get nondefs.'
    )
    args = parser.parse_args()

    cm_csv = gen(args.ground_truth, args.results, args.properties)

    cm_csv = [cm_csv[0]] + sorted(cm_csv[1:])
    csv.writer(sys.stdout).writerows(cm_csv)
