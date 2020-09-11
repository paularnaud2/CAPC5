from SQL.init import init, init_gko
from SQL.functions import process_range_list, process_gko_query, finish
from SQL.rg import *
import SQL.gl
from threading import Thread

def export_strd():
	
	init()
	
	var = get_var_name(gl.query)
	range_list = gen_range_list(var)
	range_list = restart(range_list)
	process_range_list(range_list, var)
	if gl.MERGE_RG_FILES or not gl.bools['RANGE_QUERY']:
		merge_tmp_files()
	else:
		move_tmp_folder()
		
	finish()
	
def export_gko():
	
	init()
	inst_list = init_gko()
	
	thread_list = []
	for inst in inst_list:
		th = Thread(target=process_gko_query, args=(inst,))
		#th = Thread(process_gko_query(inst))
		thread_list.append(th)
		th.start()
	
	for th in thread_list:
		th.join()
	
	merge_tmp_files()
	
	finish()