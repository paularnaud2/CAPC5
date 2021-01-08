from . import g
from os import listdir
from os.path import join
from os.path import isfile
from time import sleep
from shutil import rmtree


def delete_folder(path):
    rmtree(path)
    sleep(0.5)


def merge_files(in_dir, out_dir, remove_header=False):
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        with open(out_dir, 'a', encoding='utf-8') as out_file:
            i = 0
            for line in in_file:
                i += 1
                if remove_header and i == 1:
                    pass
                else:
                    out_file.write(line)


def get_file_list(in_dir):
    try:
        file_list = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]
    except FileNotFoundError:
        return []

    file_list.sort()
    return file_list


def load_txt(in_dir, list_out=True):
    g.counters["txt_read"] = 0
    out = []
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            out.append(line)
            g.counters["txt_read"] += 1
    if list_out is False:
        s = ''
        for line in out:
            s += line
            out = s
    return out


def count_lines(in_dir):
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        i = 0
        for line in in_file:
            i += 1

    return i


def get_header(in_dir):

    with open(in_dir, 'r', encoding='utf-8') as in_file:
        header = in_file.readline()

    return header


def save_list(list, out_file_dir):
    with open(out_file_dir, 'w', encoding='utf-8') as out_file:
        for elt in list:
            out_file.write(str(elt).strip("\n") + '\n')


def read_file(in_dir):
    with open(in_dir, 'r', encoding='utf-8') as in_file:
        txt = in_file.read()
    return txt
