from common import *
init_log('QDD')

import QDD.gl
from QDD.main import *
from QDD.init import set_dirs
from Tools.split import split_file_main

def runQDD():
	
	log("Package QDD - Début du traitement\n", print_date = True)
	start_time = time()
	dirs = set_dirs()
	
	check_py_version(dirs["in1"])
	sort_file(dirs["in1"], dirs["out1"], True, 1)
	sort_file(dirs["in2"], dirs["out2"], True, 2)
	compare_sorted_files_main(dirs["out1"], dirs["out2"], dirs["out"])
	split_file_main(dirs["out"], gl.MAX_LINE_SPLIT, True, True, gl.counters["out"])
	
	s = "Exécution terminée en {}"
	duration = get_duration_ms(start_time)
	s = s.format(get_duration_string(duration))
	log(s)
	send_notif(s, "QDD", duration)
	print_com("")