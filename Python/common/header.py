from . import g
from .csv import csv_to_list


def get_header(in_dir):
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        header = in_file.readline().strip('\n')

    return header


def gen_header(in_dir, last_field='', out_dir=''):

    if has_header(in_dir):
        header = get_header(in_dir)
    else:
        with open(in_dir, 'r', encoding='utf-8') as in_file:
            line_list = csv_to_list(in_file.readline())

        header = g.DEFAULT_FIELD + "_1"
        if len(line_list) > 1:
            counter = 1
            for elt in line_list[1:]:
                counter += 1
                header = f'{header}{g.CSV_SEPARATOR}{g.DEFAULT_FIELD}_{counter}'

    if last_field:
        header = header + g.CSV_SEPARATOR + last_field

    if out_dir:
        with open(out_dir, 'w', encoding='utf-8') as out_file:
            out_file.write(header)

    return header


def has_header(in_var):
    out = True
    if isinstance(in_var, str):
        ar = []
        with open(in_var, 'r', encoding='utf-8') as in_file:
            ar.append(csv_to_list(in_file.readline()))
            ar.append(csv_to_list(in_file.readline()))
    else:
        ar = in_var

    if isinstance(ar[0], str):
        if len(ar[0]) == len(ar[1]):
            out = False
    else:
        if len(ar[0][0]) == len(ar[1][0]):
            out = False

    return out
