import argparse
import csv
import sys


CM_HEADER = ["property", "version", "result"]


def get_result(t, r):
    if t == 0:
        if r[0] == 'N':
            return 'T' + r  # TN
        else:
            return 'F' + r  # FP
    else:
        if r[0] == 'N':
            return 'F' + r  # FN
        else:
            return 'T' + r  # TP


def gen(ground_truth_csv, results_csv):
    rows = [CM_HEADER]
    truths = {}     # (p,v): truth
    
    with open(ground_truth_csv, 'r') as gt:
        gt_reader = csv.reader(gt)

        next(gt_reader)

        for row in gt_reader:
            p, v, t = row[0], row[1], row[2]
            truths.update({(p,v): t})

    with open(results_csv, 'r') as res:
        res_reader = csv.reader(res)

        next(res_reader)

        for row in res_reader:
            p, v, r = row[0], row[1], row[2]
            try:
                rows.append([p, v, get_result(int(truths[(p,v)]), r)])
            except KeyError as e:
                print("\n[Error]: cm_gen.py:" +
                      " Missing lines in ground-truth.csv:",
                      e,
                      file=sys.stderr)
                sys.exit(1)


    return rows


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
    args = parser.parse_args()

    cm_csv = gen(args.ground_truth, args.results)

    cm_csv = [cm_csv[0]] + sorted(cm_csv[1:])
    csv.writer(sys.stdout).writerows(cm_csv)
