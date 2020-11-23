from datetime import datetime
from math import floor
from time import time
from os import listdir, remove, makedirs
from os.path import isfile, join, exists
from shutil import copyfile, rmtree
from threading import RLock

verrou = RLock()

LOG_LEVEL = 1
LOG_OUT = 'C:/Py/OUT/TMP/LOG/'
LOG_ARC = 'C:/Py/OUT/TMP/LOG/LOG_ARC/'
TMP_PATH_SQL = 'C:/Py/OUT/TMP/SQL/'
TMP_PATH_TOOLS = 'C:/Py/OUT/TMP/Tools/'
TMP_PATH_REQLIST = 'C:/Py/OUT/TMP/ReqList/'
TMP_PATH_QDD = 'C:/Py/OUT/TMP/QDD/'
PY_IN = 'C:/Py/IN/'
LOG_FILE = ''
LOG_OUTPUT = True
LOG_FILE_INITIALISED = False
MAX_LOG_FILES = 50
MIN_ARC_GRP = 50
CSV_SEPARATOR = ';'
MIN_DUR_NOTIF_TRIGGER = 30
start_time = time()
counters = {}
sl_time_dict = {}
sl_detail = {}

def extract_list(array_in, dir_out, col_nb = 1):
	
	if isinstance(array_in[0], str):
		out_list = array_in[1:]
	else:
		out_list = [elt[col_nb - 1] for elt in array_in[1:]]
	save_csv(out_list, dir_out)

def delete_folder(path):
	
	rmtree(path)

def send_notif(msg, package, duration = 0):

	if duration != 0:
		duration = duration/1000
		if duration < MIN_DUR_NOTIF_TRIGGER:
			return
	
	try:
		from win10toast import ToastNotifier
	except ModuleNotFoundError:
		s = "Échec de l'envoi de la notification windows. Le module win10toast n'est pas installé."
		log(s)
		return
		
	toaster = ToastNotifier()
	toaster.show_toast("Python - " + package, msg, duration = 10, threaded=True)
	log("Notification Windows envoyée")
	
def init_directories():

	if not exists(PY_IN):
		makedirs(PY_IN)
	
	if not exists(LOG_OUT):
		makedirs(LOG_OUT)
	
	if not exists(LOG_ARC):
		makedirs(LOG_ARC)
	
	if not exists(TMP_PATH_SQL):
		makedirs(TMP_PATH_SQL)
	if not exists(TMP_PATH_TOOLS):
		makedirs(TMP_PATH_TOOLS)
	if not exists(TMP_PATH_REQLIST):
		makedirs(TMP_PATH_REQLIST)
	if not exists(TMP_PATH_QDD):
		makedirs(TMP_PATH_QDD)

def log(str_in, level = 0, print_date = False, nb_tab = 0):
	
	if LOG_LEVEL >= level:
		t = str(datetime.now().time())
		t = t[0:8]
		if print_date:
			d = str(datetime.now().date())
			s = d + ' ' + t
		else:
			s = t
		s = s + " - " + str_in
		print_com(s, nb_tab)

def get_date():
	
	d = str(datetime.now().date())
	
	return d

def print_com(str_in, nb_tab = 0):

	if nb_tab != 0:
		for i in range(0, nb_tab):
			str_in = '\t' + str_in
		
	with verrou:
		print(str_in)
		write_log(str_in)

def print_array(array, nb_tab = 0):
	
	for elt in array:
		print_com(elt, nb_tab)

def print_dict(dict):
	
	for elt in dict:
		print('{} : {}'.format(elt, dict[elt]))

def write_log(str_in):
	
	if not LOG_OUTPUT:
		return
	
	s = str(str_in)
	with open(LOG_OUT + LOG_FILE, 'a', encoding='utf-8') as in_file:
		in_file.write(s + '\n')

def input_com(str_in):

	command = input(str_in)
	write_log(str_in + command)
	
	return command

def merge_files(in_dir, out_dir, remove_header = False):
	
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
	
def arc_log_files():
	
	file_list = get_file_list(LOG_OUT)
	if len(file_list) > MAX_LOG_FILES + MIN_ARC_GRP:
		log("Archivage des fichiers de log...")
		counter = 0
		while len(file_list) > MAX_LOG_FILES:
			copyfile(LOG_OUT + file_list[0], LOG_ARC + file_list[0])
			remove(LOG_OUT + file_list[0])
			del file_list[0]
			counter += 1
		s = "{} fichiers de log archivés. {} restants dans le dossier courant."
		s = s.format(counter, MAX_LOG_FILES)
		log(s)

def init_log(parent_module):
	
	global LOG_FILE, LOG_FILE_INITIALISED
	
	if LOG_FILE_INITIALISED:
		return
	
	init_directories()
	
	t = str(datetime.now().time())
	t = t[0:8].replace(':', '')
	d = str(datetime.now().date())
	d = d.replace('-', '')
	LOG_FILE = d + t + '_' + parent_module + '.txt'
	with open(LOG_OUT + LOG_FILE, 'w', encoding='utf-8') as in_file:
		in_file.write('')
	
	log("Fichier de log initialisé ({})".format(LOG_OUT + LOG_FILE), print_date = True)
	arc_log_files()
	LOG_FILE_INITIALISED = True
	
def get_csv_fields_dict(in_dir):
	
	fields = {}
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		header = in_file.readline()
	
	line_list = csv_to_list(header)
	for i, elt in enumerate(line_list):
		fields[elt] = i
	
	return fields

def get_csv_fields_list(in_dir):
	
	fields = {}
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		header = in_file.readline()
	
	line_list = csv_to_list(header)
	
	return line_list

def load_csv(in_dir):
	
	counters["csv_read"] = 0
	out_list = []	
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		for line in in_file:
			line_list = csv_to_list(line)
			if len(line_list) == 1:
				line_list = line_list[0]
			out_list.append(line_list)
			counters["csv_read"] += 1
	
	return out_list
	
def csv_to_list(line_in):

	txt = line_in.strip("\n\ufeff")
	line_list = txt.split(CSV_SEPARATOR)
	return line_list
	
def load_txt(in_dir):
	
	counters["txt_read"] = 0
	out_list = []	
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		for line in in_file:
			out_list.append(line)
			counters["txt_read"] += 1
	return out_list

def save_csv(array_in, out_file_dir, att = 'w'):
	
	with open(out_file_dir, att, encoding='utf-8') as out_file:
		for row in array_in:
			write_csv_line(row, out_file)

def write_csv_line(row, out_file):
	
	if isinstance(row, str):
		out_file.write(row + '\n')
		return
	
	line_out = str(row[0])
	for elt in row[1:]:   
		line_out += CSV_SEPARATOR + str(elt)
	line_out += '\n'
	out_file.write(line_out)

def get_duration_string(duration_ms):
	
	if duration_ms >= 1000:
		duration_s = duration_ms/1000
		if duration_s > 60:
			duration_m = duration_s//60
			duration_s = duration_s%60
			out = str(floor(duration_m)) + " minutes et " + str(floor(duration_s)) + " secondes"
			return(out)
		out = str(duration_s) + " secondes"
		return(out)
	out = str(duration_ms) + " ms"
	return(out)

def get_duration_ms(start_time, end_time = ""):
	
	if end_time == "":
		end_time = time()
		
	duration = floor((end_time - start_time) * 1000)
	
	return duration

def big_number(str_in):
	
	s = str(str_in)
	position = len(s)
	counter = 0
	out = ""
	while position != 0:
		counter += 1
		position -= 1
		out = s[position] + out
		if counter % 3 == 0 and position != 0:
			out = " " + out
	return(out)

def gen_sl_detail(range_name, th_nb = 1, what = 'la plage', multi_thread = False):
	global sl_detail
	
	th_name = str(range_name) + '_' + str(th_nb) 
	
	if range_name not in ['', 'MONO'] and multi_thread == True:
		detail = ' pour {} {} (pool No.{})'.format(what, range_name, th_nb)
	elif range_name not in ['', 'MONO']:
		detail = ' pour {} {}'.format(what, range_name)
	elif multi_thread == True:
		detail = ' (pool No.{})'.format(th_nb)
	else:
		detail = ''
	
	with verrou:
		sl_detail[th_name] = detail
	
	init_sl_time(th_name)
	return th_name

def step_log(counter, step, what = 'lignes écrites', nb = 0, th_name = 'DEFAULT'):
	# Pour une utilisation simple, initialiser avec init_sl_time()
	# Pour une utilisation multi_thread, initialiser avec gen_sl_detail(range_name)
	global sl_time_dict
	
	if counter % step != 0:
		return False
	
	try:
		detail = sl_detail[th_name]
	except KeyError:
		detail = ''
		
	st = sl_time_dict[th_name]
	duration_ms = get_duration_ms(st)
	ds = get_duration_string(duration_ms)
	bn_1 = big_number(step)
	bn_2 = big_number(counter)
	if nb == 0:
		s = "{bn1} {what} en {ds}. {bn2} {what} au total{detail}."
		s = s.format(bn1 = bn_1, bn2 = bn_2, ds = ds, what = what, detail = detail)
	else:
		bn_3 = big_number(nb)
		s = what.format(bn_1 = bn_1, ds = ds, bn_2 = bn_2, bn_3 = bn_3)

	log(s)
	init_sl_time(th_name)
	
	return True
	
def init_sl_time(th_name = 'DEFAULT'):
	global sl_time_dict
	
	with verrou:
		sl_time_dict[th_name] = time()

def split_array(array_in, max_elt):
	array_out = []
	cur_array = array_in[0:max_elt]
	i = 0
	while cur_array != []:
		i += 1
		array_out.append(cur_array)
		cur_array = array_in[max_elt*i:max_elt*(i+1)]
	
	return array_out

def count_lines(in_dir):
	
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		i = 0
		for line in in_file:
			i += 1
	
	return i

def get_header(in_dir):

	with open(in_dir, 'r', encoding='utf-8') as in_file:
		header  = in_file.readline()
		
	return header

def reverse_string(str_in):

	str_out = "" 
	for i in str_in: 
		str_out = i + str_out
		
	return str_out

def save_list(list, out_file_dir):

	with open(out_file_dir, 'w', encoding='utf-8') as out_file:
		for elt in list:
			out_file.write(str(elt).strip("\n") + '\n')
		
def read_file(in_dir):

	with open(in_dir, 'r', encoding='utf-8') as in_file:
		txt = in_file.read()
	return txt