import common as com
com.LOG_FILE_INITIALISED = True

def csv_to_xls():
	from Tools.csv_to_xls import csv_to_xls_folder
	com.LOG_FILE_INITIALISED = False
	com.init_log('Tools')
	com.LOG_OUTPUT = True
	csv_to_xls_folder()
	
def fdup():
	from Tools.dup import find_dup_main
	com.LOG_OUTPUT = False
	find_dup_main()

def rdup(field_nb = 0):
	from Tools.dup import remove_dup_main
	com.LOG_OUTPUT = False
	remove_dup_main(field_nb = field_nb)
	
def rbf():
	from Tools.rbf import read_big_file
	com.LOG_OUTPUT = False
	read_big_file()

def sbf():
	from Tools.sbf import search_big_file
	com.LOG_OUTPUT = False
	search_big_file()

def split():
	from Tools.split import split_file_main
	com.LOG_OUTPUT = False
	split_file_main(add_header = False, prompt = False)

def merge():
	from Tools.merge import merge_files_main
	com.LOG_OUTPUT = False
	merge_files_main()
	
def sort():
	from Tools.sort import sort_csv_file_main
	com.LOG_OUTPUT = False
	sort_csv_file_main()

def flt():
	from Tools.filter import filter_main
	com.LOG_OUTPUT = False
	filter_main()

def shuf():
	from Tools.shuf import shuffle_csv
	com.LOG_OUTPUT = False
	shuffle_csv()
	
def xml():
	from Tools.xml import parse_xml
	com.LOG_OUTPUT = False
	parse_xml()