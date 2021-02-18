import os
import qdd.gl as gl
import common as com

from time import time
from qdd.init import set_dirs
from qdd.init import init_params
from qdd.init import init_tmp_dir
from qdd.init import init_file_match
from qdd.csf import compare_headers
from qdd.csf import compare_sorted_files
from qdd.sort import sort_file
from qdd.functions import check_py_version
from qdd.functions import check_split


def run_qdd(**params):

    com.log("[qdd] run_qdd")
    start_time = time()
    init_params(params)
    init_tmp_dir()
    dirs = set_dirs()
    check_py_version(dirs["in1"])

    sort_file(dirs["in1"], dirs["out1"], True, 1)
    sort_file(dirs["in2"], dirs["out2"], True, 2)
    if not compare_files(dirs["out1"], dirs["out2"], dirs["out"]):
        com.log_print('|')
        check_split(dirs["out"])

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "qdd", duration)
    com.log_print()
    if gl.OPEN_OUT_FILE:
        os.startfile(dirs["out"])


def file_match(in1, in2, compare=False, sort=True):
    com.log("[qdd] file_match")
    s = f"Comparaison des fichiers {in1} et {in2} en cours..."
    com.log(s)
    ar1 = com.load_csv(in1)
    ar2 = com.load_csv(in2)
    if sort:
        ar1.sort()
        ar2.sort()
    if compare:
        init_file_match()
        com.save_csv(ar1, gl.TMP_1)
        com.save_csv(ar2, gl.TMP_2)
        res = compare_files(gl.TMP_1, gl.TMP_2, gl.OUT_DIR)
        if not res:
            os.startfile(gl.OUT_DIR)
    else:
        res = ar1 == ar2
        if res:
            com.log("Les deux fichiers sont identiques")
        else:
            com.log("Les deux fichiers sont différents")

    assert res is True
    com.log_print()


def compare_files(in_1, in_2, out):

    start_time = time()
    if not compare_headers(in_1, in_2):
        return False
    com.gen_header(in_1, gl.COMPARE_FIELD, out)
    compare_sorted_files(in_1, in_2, out)

    duration = com.get_duration_ms(start_time)
    ds = com.get_duration_string(duration)
    s = f"Comparaison terminée en {ds}"
    com.log(s)
    if gl.counters["diff"] == 0:
        com.log("Les deux fichiers sont identiques")
        return True
    else:
        bn = com.big_number(gl.counters["diff"])
        com.log(f"{bn} écarts trouvés")
        return False
