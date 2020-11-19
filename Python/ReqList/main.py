import ReqList.gl as gl
from ReqList.functions import *
from ReqList.join import *
from ReqList.strd import get_sql_array_out_strd
from ReqList.gko import get_sql_array_out_ginko
from SQL.init import init
from common import *
import common as com

def get_sql_array(array_in, BDD, query_file):
	
	restart()
	get_query_var(query_file)
	gen_group_list(array_in)
	export = get_export(BDD)
	return export

def get_export(BDD):
	
	init()
	print_com("|")
	log("Récupération de l'export SQL...")
	gl.header = ''
	gl.array_dict = {}
	gl.bools["EXPORT_INSTANCES"] = gl.EXPORT_INSTANCES and BDD == 'GINKO'
	
	if BDD == 'GINKO':
		array_out = get_sql_array_out_ginko()
	else:
		array_out = get_sql_array_out_strd(BDD)
	
	delete_folder(gl.TMP_PATH)
	print_com("|")
	s = "Export récupéré ({} lignes écrites)\n|"
	bn = big_number(len(array_out))
	log(s.format(bn))
	
	del gl.array_dict
	return array_out

def join_arrays(ar_left_in, ar_right_in):
	
	log("Jointure des deux tableaux (initialisation)")
	check_void_right_array(ar_right_in)
	log("Préparation du tableau de gauche...")
	(ar_left, first_line_l) = prepare_array(ar_left_in)
	save_csv(ar_left, gl.OUT_LEFT)
	log_prepare(gl.OUT_LEFT, big_number(len(ar_left)))

	log("Préparation du tableau de droite...")
	(ar_right, first_line_r) = prepare_array(ar_right_in)
	save_csv(ar_right, gl.OUT_RIGHT)
	log_prepare(gl.OUT_RIGHT, big_number(len(ar_right)))
	
	log("Jointure des deux tableaux en cours...")
	init_while_join(first_line_l, first_line_r)
	while gl.bools["end_left"] == False or gl.bools["end_right"] == False:
		(pdl_l, pdl_r) = update_pdl(ar_left, ar_right)
		pdl_l = compare_inf(pdl_l, pdl_r, ar_left)
		(pdl_l, pdl_r) = compare_sup(pdl_l, pdl_r, ar_left, ar_right)
		pdl_r = compare_equal(pdl_l, pdl_r, ar_left, ar_right)
		if incr_c_l(ar_left):
			break
	s = "Jointure effecutée. Le tableau de sortie comporte {} lignes (en-tête incluse)."
	log(s.format(big_number(len(gl.out_array))))