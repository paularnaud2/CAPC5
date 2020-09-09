import re
import Tools.gl as gl
from common import *
import math

RE_EXP = '<(.*)>(.*)</(.*)>'
IN_FILE = 'C:/Py/IN/in.xml'
IN_FILE = 'C:/Py/IN/2020_09_03_SITES.xml'
OUT_FILE = 'C:/Py/OUT/out.csv'
SL_STEP_READ = 1000 * 10**3
SL_STEP_WRITE = 100 * 10**3

def parse_xml():
	
	gl.counters['nb line read'] = 0
	
	log('Génération du dictionnaire image...')
	with open(IN_FILE, 'r', encoding='utf-8', errors='ignore') as in_file:
		line = read_file(in_file)
		fill_parse_dict(line)
		init_sl_time()
		while line != "":
			line = read_file(in_file)
			fill_parse_dict(line)
	log('Dictionnaire image généré.')
	# print('Impression du dictionnaire :')
	# print_dict(gl.parse_dict)
	
	even_dict()
	log('Sauvegarde du dictionnaire au format csv...')
	save_dict_csv(gl.parse_dict, OUT_FILE)
	log("Fichier csv généré à l'adresse {}".format(OUT_FILE))
	
	print('')
	log("Fin du traitement")

def save_dict_csv(dict, out_file_dir, att = 'w'):
	
	(min_size, max_size) = get_sizes(gl.parse_dict)
	header = []
	for elt in dict:
		header.append(elt)
	
	with open(out_file_dir, att, encoding='utf-8') as out_file:
		write_csv_line(header, out_file)
		i = 0
		init_sl_time()
		while i < max_size:
			cur_row = []
			for elt in dict:
				cur_row.append(dict[elt][i])
			write_csv_line(cur_row, out_file)
			i += 1
			step_log(i, SL_STEP_WRITE, what = 'lignes écrites')

def read_file(in_file):
	
	line = in_file.readline()
	gl.counters['nb line read'] += 1
	step_log(gl.counters['nb line read'], SL_STEP_READ, what = 'lignes traitées')
	
	return line

def get_xml(in_str):
	
	m = re.search(RE_EXP, in_str)
	if m is None:
		return []
	
	tag = m.group(1)
	elt = m.group(2)
	
	return (tag, elt)
	
def fill_parse_dict(str_in):
	
	xml_out = get_xml(str_in)
	if xml_out != []:
		# print(str_in.strip("\n"))
		(tag, elt) = xml_out
		if tag in gl.parse_dict:
			gl.parse_dict[tag].append(elt)
		else:
			gl.parse_dict[tag] = [elt]
		complete_dict()
		
def get_sizes(dict):

	min_size = math.inf
	max_size = 0
	for elt in dict:
		cur_l = len(dict[elt])
		if cur_l < min_size:
			min_size = cur_l
		if cur_l > max_size:
			max_size = cur_l
	
	return (min_size, max_size)
	
def complete_dict():

	(min_size, max_size) = get_sizes(gl.parse_dict)
	if max_size - min_size > 1:
		# print('sizes (min, max) : {}'.format((min_size, max_size)))
		for elt in gl.parse_dict:
			if len(gl.parse_dict[elt]) == min_size:
				gl.parse_dict[elt].append('')

def even_dict():

	(min_size, max_size) = get_sizes(gl.parse_dict)
	if max_size - min_size > 0:
		# print('sizes (min, max) : {}'.format((min_size, max_size)))
		for elt in gl.parse_dict:
			while len(gl.parse_dict[elt]) < max_size:
				gl.parse_dict[elt].append('')