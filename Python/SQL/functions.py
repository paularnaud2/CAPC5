# Package SQL
import common as com
import SQL.gl as gl
import SQL.log as log

from common import g
from os import rename
from threading import RLock

verrou = RLock()


def get_final_script(script_file):
    script = com.read_file(script_file)
    for key in gl.VAR_DICT:
        script = script.replace(key, gl.VAR_DICT[key])
    return script


def write_rows(cursor, range_name='MONO', th_name='DEFAULT', th_nb=0):

    log.write_rows_init(range_name, th_nb)
    with open(gl.out_files[range_name + gl.EC], 'a',
              encoding='utf-8') as out_file:
        i = 0
        for row in cursor:
            iter = write_row(row, out_file, range_name)
            i += iter
            with verrou:
                gl.counters["row"] += iter
            com.step_log(i, gl.SL_STEP, th_name=th_name)

    rename(gl.out_files[range_name + gl.EC], gl.out_files[range_name])
    log.write_rows_finish(range_name, i, th_nb)


def write_row(row, out_file, range_name='MONO'):

    line_out = gl.LEFT_DEL + str(row[0]).strip('\r\n') + gl.RIGHT_DEL
    for elt in row[1:]:
        s = str(elt)
        if s == 'None':
            s = ''
        line_out += com.CSV_SEPARATOR + gl.LEFT_DEL + s.strip(
            '\r\n') + gl.RIGHT_DEL
    if line_out.strip(g.CSV_SEPARATOR) == '':
        return 0
    if (gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES
            or gl.EXPORT_RANGE and range_name != 'MONO'):
        line_out += com.CSV_SEPARATOR + range_name
    line_out += '\n'
    out_file.write(line_out)
    return 1


def export_cursor(cursor, inst=''):

    out_list = []
    for row in cursor:
        str_row = [
            str(field).strip('\r\n') if str(field) != 'None' else ''
            for field in row
        ]
        if inst != '':
            str_row.append(inst)
        out_list.append(str_row)
        with verrou:
            gl.counters["row"] += 1

    return out_list
