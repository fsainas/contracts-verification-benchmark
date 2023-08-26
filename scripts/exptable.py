"""
Script Name: exptable
Description:
    Creates a markdown table summarizing experiment results
    from an 'out.csv' file.

Usage:
    python exptable.py -i simple_transfer/solcmc/out.csv
    -o simple_transfer_solcmc.md
"""

import argparse
import csv

min_cell_width = 5


def make_markdown_table(pset, vset, results):
    """
    Writes the markdown table as a list of rows.

    Args:
        pset (set): The set of properties.
        vset (set): The set of variants.
        results (dict): Results of experiments, the keys are (p,v) couples.

    Returns:
        list: The list of rows.
    """

    plist = sorted(list(pset))
    vlist = sorted(list(vset))

    max_p_length = max([len(plist[i]) for i in range(len(plist))])
    max_v_length = max([len(vlist[i]) for i in range(len(vlist))])

    cell_width = max(min_cell_width, max_p_length+2)    # 2 is the margin

    # Create the header row
    header = (
            "|" + " " * (max_v_length + 6) + "| " +
            "| ".join([p + " "*(cell_width-len(p)-1) for p in plist]) +
            "|"
    )
    separator = (
            "|" + "-" * (max_v_length + 6) + "|" +
            "|".join([
                "-" * len(header.split('|')[i])
                for i in range(2, len(plist) + 2)
            ]) + "|"
    )

    # Create the rows
    rows = []
    for v in vlist:
        row_str = "| **" + v + "** |"
        for p in plist:
            res = results[(p,v)]
            if res is not None:
                row_str += " " + res + " " * (cell_width-len(res)-1) + "|"
            else:
                row_str += cell_width

        rows.append(row_str)

    # Combine everything into a Markdown table
    markdown_table = "\n".join([header, separator] + rows)

    return markdown_table


def main(input_file, outputfile=True):
    '''outputfile: if it's out.csv, otherwise assume in.csv'''
    table = []

    # Read data from input file
    with open(input_file, 'r') as input:
        csv_reader = csv.reader(input)

        next(csv_reader)

        results = {}      # (p,v): res
        pset = set()
        vset = set()

        for row in csv_reader:
            if outputfile:
                p, v, _, res = row[0], row[1], row[2], row[3]
            else:
                p, v, res = row[0], row[1], row[2]

            pset.add(p)
            vset.add(v)
            results.update({(p,v): res})

        table = make_markdown_table(pset, vset, results)

    return table


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', help='CSV input file')
    parser.add_argument('--output', '-o', help='File to write to')
    args = parser.parse_args()

    input_file = args.input
    ouput_file = args.output

    table = main(args.input)

    # Eventually writes to output file
    if ouput_file is not None:
        with open(ouput_file, 'w') as file:
            file.write(table)