import common as com


def csv_to_xls():
    from tools.csv_to_xls import csv_to_xls_folder
    com.LOG_FILE_INITIALISED = False
    com.init_log('tools')
    com.LOG_OUTPUT = True
    csv_to_xls_folder()


def fdup():
    from tools.dup import find_dup_main
    com.LOG_OUTPUT = False
    find_dup_main()


def rdup(field_nb=0):
    from tools.dup import remove_dup_main
    com.LOG_OUTPUT = False
    remove_dup_main(field_nb=field_nb)


def rbf():
    from tools.rbf import read_big_file
    com.LOG_OUTPUT = False
    read_big_file()


def sbf():
    from tools.sbf import search_big_file
    com.LOG_OUTPUT = False
    search_big_file()


def split():
    from tools.split import split_file_main
    com.LOG_OUTPUT = False
    split_file_main(add_header=False, prompt=False)


def merge():
    from tools.merge import merge_files_main
    com.LOG_OUTPUT = False
    merge_files_main()


def sort():
    from tools.sort import sort_csv_file_main
    com.LOG_OUTPUT = False
    sort_csv_file_main()


def flt():
    from tools.filter import filter_main
    com.LOG_OUTPUT = False
    filter_main()


def shuf():
    from tools.shuf import shuffle_csv
    com.LOG_OUTPUT = False
    shuffle_csv()


def xml():
    from tools.xml import parse_xml
    # com.LOG_FILE_INITIALISED = True
    com.LOG_OUTPUT = False
    parse_xml()
