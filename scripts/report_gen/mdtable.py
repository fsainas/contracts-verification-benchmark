'''
Creates a markdown table from a csv file with this scheme: cols, rows, data.

Usage:
    python mdtable_gen.py --input file.csv
'''

import argparse
import logging
import csv
import sys


MIN_CELL_WIDTH = 7
MARGIN = 2   # between cells


def gen_from_dict(data):
    '''
    Writes the markdown table as a list of rows.

    Args:
        data (dict): { (col, row): (data, footnote) }

    Returns:
        str: markdown table
    '''

    cols_ids = sorted(set([c for c, _ in data.keys()]))
    rows_ids = sorted(set([r for _, r in data.keys()]))

    if not rows_ids:
        logging.error('Empty cm.csv file.')
        sys.exit(1)

    max_c_length = max([len(c) for c in cols_ids])
    max_r_length = max([len(r) for r in rows_ids])

    cell_width = max(
            MIN_CELL_WIDTH,
            max_c_length + MARGIN,
            max_r_length + MARGIN
    )

    # Create the header row
    header = (
            '|' + ' ' * (max_r_length + 6) + '| ' +
            '| '.join([c + ' '*(cell_width-len(c)-1) for c in cols_ids]) +
            '|'
    )
    separator = (
            '|' + '-' * (max_r_length + 6) + '|' +
            '|'.join([
                '-' * len(header.split('|')[i])
                for i in range(2, len(cols_ids) + 2)
            ]) + '|'
    )

    # Create the rows
    table_rows = []
    fn_rows = []        # footnotes to put at the end of the table
    fn_counter = 1      # next free footnote index
    for r in rows_ids:
        row = '| **' + r + '** |'   # row index in bold
        for c in cols_ids:
            d, fn = data[(c, r)]
            if d:   # if there is data add it to the table
                if len(fn) > 0:
                    fn_mark = '[^' + str(fn_counter) + ']'        # e.g. [^1]
                    row += ' ' + d + fn_mark + ' ' * (cell_width-len(d+fn_mark)-1) + '|'
                    fn_counter += 1
                    fn_rows.append(fn_mark + ': ' + fn)
                else:
                    row += ' ' + d + ' ' * (cell_width-len(d)-1) + '|'
            else:   # else preserve spaces
                row += cell_width

        table_rows.append(row)

    # Combine everything into a Markdown table
    mdtable = '\n'.join([header, separator] + table_rows + [' '] + fn_rows) + '\n'

    return mdtable


def gen_from_csv(input_file):
    mdtable = []

    # Read data from input file
    with open(input_file, 'r') as f:
        csv_reader = csv.reader(f)

        first_row = next(csv_reader)

        if not first_row:
            logging.error(f'{input_file} is empty.')
            sys.exit(1)

        data = {}      # (c,r): (data, footnote)

        for row in csv_reader:
            # skip blank lines or comments
            if not row or row[0] == '#':
                continue

            c, r, d = row[0], row[1], row[2]

            if len(c) == 0 or len(r) == 0 or len(d) == 0:
                logging.error(f'Missing values in {input_file}.\n'
                              f'-> {c},{r},{d}')
                sys.exit(1)

            fn = row[3] if len(row) == 4 else ''    # footnote

            data.update({(c, r): (d, fn)})

        mdtable = gen_from_dict(data)

    return mdtable
