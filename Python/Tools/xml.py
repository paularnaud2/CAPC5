import re
import Tools.gl as gl
import os
from common import *
import common as com
import math

RE_EXP_TAG_ELT = '<(.*)>(.*)</(.*)>'
RE_EXP_SUB_TAG = '<([a-z][^<]*[a-z])>$'
IN_FILE = 'C:/Py/IN/in - test.xml'
# IN_FILE = 'C:/Py/IN/Enedis_APR_20201101_115205318.xml'
OUT_FILE = 'C:/Py/OUT/out.csv'
SL_STEP_READ = 1000 * 10**3
SL_STEP_WRITE = 100 * 10**3
FIRST_TAG = ''
SUB_TAG = ''
MULTI_TAG_LIST = ['libelle', 'civilite', 'nom', 'prenom', 'telephone1Num', 'telephone2Num', 'adresseEmail']
N_ROW = 0

def parse_xml():
	
	gen_img_dict()
	save_img_dict(gl.parse_dict, OUT_FILE)
	finish()
	
def finish():
	
	dur = get_duration_ms(gl.start_time)
	bn = big_number(gl.counters["write"])
	s = "Parsing terminé. {} lignes écrites en {}."
	s = s.format(bn, get_duration_string(dur))
	log(s)
	os.startfile(OUT_FILE)
	
def gen_img_dict():
	
	log('Génération du dictionnaire image à partir du fichier {}...'.format(IN_FILE))
	with open(IN_FILE, 'r', encoding='utf-8', errors='ignore') as in_file:
		gl.counters['read'] = 0
		line = read_one_line(in_file)
		fill_parse_dict(line)
		init_sl_time()
		while line != "":
			line = read_one_line(in_file)
			fill_parse_dict(line)
	
	even_dict()
	log('Dictionnaire image généré.')
	print('')

def save_img_dict(dict, out_file_dir, att = 'w'):
	
	log('Sauvegarde du dictionnaire au format csv...')
	header = []
	for elt in dict:
		header.append(elt)
	
	with open(out_file_dir, att, encoding='utf-8') as out_file:
		write_csv_line(header, out_file)
		init_sl_time()
		gl.counters['write'] = 0
		while gl.counters['write'] < N_ROW:
			cur_row = []
			for elt in dict:
				cur_row.append(dict[elt][gl.counters['write']])
			write_csv_line(cur_row, out_file)
			gl.counters['write'] += 1
			step_log(gl.counters['write'], SL_STEP_WRITE, what = 'lignes écrites')
			
	log("Fichier csv généré à l'adresse {}".format(OUT_FILE))
	print('')

def read_one_line(in_file):
	
	line = in_file.readline()
	gl.counters['read'] += 1
	step_log(gl.counters['read'], SL_STEP_READ, what = 'lignes traitées')
	
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
			if N_ROW > 1 and gl.parse_dict != {}: # on rencontre un nouvel élément (absent dans la première boucle)
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
	
	if not m2 is None:
		SUB_TAG = m2.group(1)
		
	if m1 is None:
		return []
	
	tag = m1.group(1)
	elt = m1.group(2)
	elt = elt.replace(com.CSV_SEPARATOR, '')
	
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
		l = len(gl.parse_dict[tag])
		if l < N_ROW - 1:
			gl.parse_dict[tag].append('')
		elif l >= N_ROW and tag != FIRST_TAG:
			s = "Attention, la balise '{}' apparaît en doublon (id = {}). Elle doit être ajoutée à la liste 'MULTI_TAG_LIST'"
			print(s.format(tag, gl.parse_dict[FIRST_TAG][N_ROW-3]))
			import sys
			sys.exit()
	
def even_dict():

	for tag in gl.parse_dict:
		n = len(gl.parse_dict[tag])
		if n < N_ROW:
			gl.parse_dict[tag].append('')