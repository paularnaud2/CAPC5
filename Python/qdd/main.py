import os
import qdd.gl as gl
import common as com

from time import time
from common import g
from tools.split import split
from qdd.init import set_dirs
from qdd.init import init_params
from qdd.init import init_out_file
from qdd.init import init_file_match
from qdd.csf import check_in_files
from qdd.csf import compare_sorted_files
from qdd.sort import sort_file
from qdd.functions import check_py_version


def run_qdd(**params):

    com.log("[qdd] run_qdd")
    start_time = time()
    init_params(params)
    dirs = set_dirs()

    check_py_version(dirs["in1"])
    sort_file(dirs["in1"], dirs["out1"], True, 1)
    sort_file(dirs["in2"], dirs["out2"], True, 2)
    if not compare_files(dirs["out1"], dirs["out2"], dirs["out"]):
        com.log_print('|')
        split(dirs["out"], gl.MAX_LINE_SPLIT, True, True, gl.counters["out"])

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "qdd", duration)
    com.log_print('')
    if gl.OPEN_OUT_FILE:
        os.startfile(dirs["out"])


def file_match(in1, in2, diff_out='', err=True, sort=True):
    com.log("[qdd] file_match")
    s = f"Comparaison des fichiers {in1} et {in2} en cours..."
    com.log(s)
    init_file_match()
    if sort:
        arr1 = sorted(com.load_csv(in1))
        in1 = gl.TMP_SORTED_1
        com.save_csv(arr1, in1)
        arr2 = sorted(com.load_csv(in2))
        in2 = gl.TMP_SORTED_2
        com.save_csv(arr2, in2)
    if diff_out == '':
        diff_out = g.paths['OUT'] + 'file_match_out.csv'
    res = compare_files(in1, in2, diff_out)
    if err and not res:
        os.startfile(diff_out)
        assert res is True
    com.log_print('')
    return res


def compare_files(in_1, in_2, out):

    start_time = time()
    header = check_in_files(in_1, in_2, out)
    if not header:
        return False
    init_out_file(out, header, gl.COMPARE_FIELD)
    compare_sorted_files(in_1, in_2, out)

    duration = com.get_duration_ms(start_time)
    ds = com.get_duration_string(duration)
    s = f"Comparaison terminée en {ds}"
    com.log(s)
    if gl.counters["diff"] == 0:
        s = "Les deux fichiers sont identiques"
        com.log(s)
        return True
    else:
        bn = com.big_number(gl.counters["diff"])
        s = f"{bn} écarts trouvés"
        com.log(s)
        return False
