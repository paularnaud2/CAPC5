import common as com
com.LOG_FILE_INITIALISED = True

from Tools.dup import find_dup_main
from Tools.dup import remove_dup_main
from Tools.rbf import read_big_file
from Tools.sbf import search_big_file
from Tools.split import split_file_main
from Tools.sort import sort_csv_file_main
from Tools.filter import filter_main
from Tools.shuf import shuffle_csv
from Tools.xml import parse_xml
from Tools.csv_to_xls import *

def csv_to_xls():
	com.LOG_FILE_INITIALISED = False
	com.init_log('Tools')
	com.LOG_OUTPUT = True
	csv_to_xls_folder()
	
def fdup():
	com.LOG_OUTPUT = False
	find_dup_main()

def rdup(field_nb = 0):
	com.LOG_OUTPUT = False
	remove_dup_main(field_nb = field_nb)
	
def rbf():
	com.LOG_OUTPUT = False
	read_big_file()

def sbf():
	com.LOG_OUTPUT = False
	search_big_file()

def split():
	com.LOG_OUTPUT = False
	split_file_main(add_header = False, prompt = False)
	
def sort():
	com.LOG_OUTPUT = False
	sort_csv_file_main()

def flt():
	com.LOG_OUTPUT = False
	filter_main()

def shuf():
	com.LOG_OUTPUT = False
	shuffle_csv()
	
def xml():
	com.LOG_OUTPUT = False
	parse_xml()