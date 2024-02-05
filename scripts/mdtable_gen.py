from report_gen.mdtable import gen_from_csv
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # cm.csv
    parser.add_argument(
            '--input',
            '-i',
            help='CSV input file',
            required=True)
    args = parser.parse_args()

    mdtable = gen_from_csv(args.input)

    print(mdtable)
