import re
import os
import common as com
import tools.gl as gl

from common import g

IN_DIR = 'test/tools/in.xml'
OUT_DIR = 'C:/Py/OUT/out.csv'

RE_EXP_TAG_ELT = '<(.*)>(.*)</(.*)>'
RE_EXP_SUB_TAG = r'<(\w[^<]*\w)>$'
SL_STEP_READ = 1000 * 10**3
SL_STEP_WRITE = 100 * 10**3
FIRST_TAG = ''
SUB_TAG = ''
MULTI_TAG_LIST = [
    'libelle',
    'civilite',
    'nom',
    'prenom',
    'telephone1Num',
    'telephone2Num',
    'adresseEmail',
]
N_ROW = 0


def parse_xml(in_dir, out_dir, open_out_file=False):

    gen_img_dict(in_dir)
    save_img_dict(gl.parse_dict, out_dir)
    finish(out_dir, open_out_file)


def finish(out_dir, open_out_file):

    dur = com.get_duration_ms(gl.start_time)
    bn = com.big_number(gl.counters["write"])
    s = "Parsing terminé. {} lignes écrites en {}."
    s = s.format(bn, com.get_duration_string(dur))
    com.log(s)
    if open_out_file:
        os.startfile(out_dir)


def gen_img_dict(in_dir):

    s = f'Génération du dictionnaire image à partir du fichier {in_dir}...'
    com.log(s)
    with open(in_dir, 'r', encoding='utf-8', errors='ignore') as in_file:
        gl.counters['read'] = 0
        line = read_one_line(in_file)
        fill_parse_dict(line)
        com.init_sl_time()
        while line != '':
            line = read_one_line(in_file)
            fill_parse_dict(line)

    even_dict()
    com.log('Dictionnaire image généré.')
    print('')


def save_img_dict(dict, out_dir, att='w'):

    com.log('Sauvegarde du dictionnaire au format csv...')
    header = []
    for elt in dict:
        header.append(elt)

    with open(out_dir, att, encoding='utf-8') as out_file:
        com.write_csv_line(header, out_file)
        com.init_sl_time()
        gl.counters['write'] = 0
        while gl.counters['write'] < N_ROW:
            cur_row = []
            for elt in dict:
                cur_row.append(dict[elt][gl.counters['write']])
            com.write_csv_line(cur_row, out_file)
            gl.counters['write'] += 1
            com.step_log(gl.counters['write'],
                         SL_STEP_WRITE,
                         what='lignes écrites')

    com.log("Fichier csv généré à l'adresse {}".format(out_dir))
    print('')


def read_one_line(in_file):

    line = in_file.readline()
    gl.counters['read'] += 1
    com.step_log(gl.counters['read'], SL_STEP_READ, what='lignes traitées')

    return line


def fill_parse_dict(str_in):
    global FIRST_TAG, N_ROW

    xml_out = get_xml(str_in)
    if xml_out != []:
        (tag, elt) = xml_out
        if tag in MULTI_TAG_LIST:
            tag = tag + '_' + SUB_TAG
        if tag in gl.parse_dict:
            gl.parse_dict[tag].append(elt)
            if tag == FIRST_TAG:
                N_ROW += 1
                complete_dict()
        else:
            if N_ROW > 1 and gl.parse_dict != {}:
                # on rencontre un nouvel élément
                # (absent dans la première boucle)
                new_col = gen_void_list(N_ROW - 1)
                new_col.append(elt)
                gl.parse_dict[tag] = new_col
            else:
                gl.parse_dict[tag] = [elt]
                if len(gl.parse_dict) == 1:
                    FIRST_TAG = tag
                    N_ROW = 1


def get_xml(in_str):
    global SUB_TAG

    m1 = re.search(RE_EXP_TAG_ELT, in_str)
    m2 = re.search(RE_EXP_SUB_TAG, in_str)

    if m2 is not None:
        SUB_TAG = m2.group(1)

    if m1 is None:
        return []

    tag = m1.group(1)
    elt = m1.group(2)
    elt = elt.replace(g.CSV_SEPARATOR, '')

    return (tag, elt)


def gen_void_list(size):

    i = 0
    out_list = []
    while i < size:
        i = i + 1
        out_list.append('')

    return out_list


def complete_dict():

    for tag in gl.parse_dict:
        n = len(gl.parse_dict[tag])
        if n < N_ROW - 1:
            gl.parse_dict[tag].append('')
        elif n >= N_ROW and tag != FIRST_TAG:
            s = "Attention, la balise '{}' apparaît en doublon (id = {})."
            s += " Elle doit être ajoutée à la liste 'MULTI_TAG_LIST'"
            print(s.format(tag, gl.parse_dict[FIRST_TAG][N_ROW - 3]))
            import sys
            sys.exit()


def even_dict():

    for tag in gl.parse_dict:
        n = len(gl.parse_dict[tag])
        if n < N_ROW:
            gl.parse_dict[tag].append('')


if __name__ == '__main__':
    parse_xml(IN_DIR, OUT_DIR, True)
