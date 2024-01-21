import argparse
import logging
import utils
from utils import ERROR
import glob
import re
import csv
import sys


CM_HEADER = ["property", "version", "result", "footnote"]


def get_result(gt: int, out: str) -> str:
    if out == ERROR:
        return ERROR
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


def gen(ground_truth_csv: str, out_csv: str, properties_dir: str) -> list[str]:
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

        # set of non definable properties, used to put the footnote once
        nondef_properties = set()

        # build confusion matrix
        for row in gt_reader:
            # skip blank lines or comments
            if not row or row[0] == '#':
                continue

            p, v, gt = row[0], row[1], int(row[2])

            if (p,v) in outputs:
                out = outputs[(p,v)]

                if out == utils.NONDEFINABLE and properties_dir:

                    # Check for a bound property first
                    bound_nondef = glob.glob(f'{properties_dir}/*{p}_{v}*')
                    if bound_nondef:
                        nondef_p = bound_nondef[0]
                    else:
                        nondef_p = glob.glob(f'{properties_dir}/*{p}.*')[0]     # take the generic one otherwise

                    if nondef_p not in nondef_properties:

                        with open(nondef_p, 'r') as file:

                            note_match = re.search('/// @custom:nondef (.*)', file.read())

                            if note_match:
                                note = note_match.group(1)
                                cm_rows.append([p, v, out, note])
                                nondef_properties.add(nondef_p)
                            else:
                                logging.warning(f'{p} is nondefinable (ND) but no note was found.')
                                cm_rows.append([p, v, out])

                    else:
                        cm_rows.append([p, v, out])

                else:
                    cm_rows.append([p, v, get_result(gt, out)])

                del outputs[(p,v)]

            else:
                cm_rows.append([p, v, utils.NONDEFINABLE])  # no file
    
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
    parser.add_argument(
            '--properties',
            '-p',
            help='Properties directory, to get nondefs.',
            #required=True
    )
    args = parser.parse_args()

    cm_csv = gen(args.ground_truth, args.results, args.properties)

    cm_csv = [cm_csv[0]] + sorted(cm_csv[1:])
    csv.writer(sys.stdout).writerows(cm_csv)
