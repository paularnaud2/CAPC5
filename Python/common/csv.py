from . import g


def get_csv_fields_dict(in_dir):
    fields = {}
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        header = in_file.readline()

    line_list = csv_to_list(header)
    for i, elt in enumerate(line_list):
        fields[elt] = i

    return fields


def get_csv_fields_list(in_dir):
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        header = in_file.readline()

    line_list = csv_to_list(header)

    return line_list


def load_csv(in_dir):
    g.counters["csv_read"] = 0
    out_list = []
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            line_list = csv_to_list(line)
            if len(line_list) == 1:
                line_list = line_list[0]
            out_list.append(line_list)
            g.counters["csv_read"] += 1

    return out_list


def csv_to_list(line_in):
    txt = line_in.strip("\n\ufeff")
    line_list = txt.split(g.CSV_SEPARATOR)
    return line_list


def save_csv(array_in, out_file_dir, att='w'):
    with open(out_file_dir, att, encoding='utf-8') as out_file:
        for row in array_in:
            write_csv_line(row, out_file)


def write_csv_line(row, out_file):
    if isinstance(row, str):
        out_file.write(row + '\n')
        return

    line_out = g.CSV_SEPARATOR.join(row)
    line_out += '\n'
    out_file.write(line_out)


def extract_list(array_in, dir_out, col_nb=1):
    out_list = []
    if isinstance(array_in[0], str):
        out_list = array_in[1:]
    else:
        # out_list = [elt[col_nb - 1] for elt in array_in[1:]]
        for elt in array_in[1:]:
            out_list.append(elt[col_nb - 1])

    save_csv(out_list, dir_out)


def csv_clean(s):
    out = s.replace('\r', '')
    out = out.replace('\n', '')
    out = out.replace(g.CSV_SEPARATOR, '')
    return out
