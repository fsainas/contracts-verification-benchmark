import argparse
import csv
import sys


CM_HEADER = ["property", "version", "result"]


def get_result(gt: int, out: str) -> str:
    if gt == 0:
        if out[0] == 'N':       # e.g 'N!'[0]
            return 'T' + out    # TN
        else:
            return 'F' + out    # FP
    else:
        if out[0] == 'N':
            return 'F' + out    # FN
        else:
            return 'T' + out    # TP


def gen(ground_truth_csv: str, out_csv: str) -> list[str]:
    cm_rows = [CM_HEADER]
    outputs = {}    # (p,v): output

    # get results
    with open(out_csv, 'r') as file:
        out_reader = csv.reader(file)
        next(out_reader)    # skip header

        for row in out_reader:
            p, v, out = row[0], row[1], row[2]
            outputs.update({(p,v): out})
    
    with open(ground_truth_csv, 'r') as file:
        gt_reader = csv.reader(file)
        next(gt_reader)     # skip header

        # build confusion matrix
        for row in gt_reader:
            if row[0] == '#':
                continue;
            p, v, gt = row[0], row[1], int(row[2])

            if (p,v) in outputs:
                out = outputs[(p,v)]
                cm_rows.append([p, v, get_result(gt, out)])
                del outputs[(p,v)]
            else:
                cm_rows.append([p, v, 'ND'])
    
    for p,v in outputs.keys():
        print(f'\n[WARNING]: missing {p}-{v} ground truth',
              file=sys.stderr)

    return cm_rows


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
