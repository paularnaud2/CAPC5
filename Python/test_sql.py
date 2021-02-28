import sql
import qdd as q
import common as com

from test import gl
from test import ttry
from time import sleep
from common import g

from multiprocessing import Process
from multiprocessing import Manager


def execute():
    sql.execute(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_CREATE_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        PROC=True,
    )


def upload(inp, test_restart=False, md=''):
    sql.upload(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_INSERT_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        UPLOAD_IN=inp,
        NB_MAX_ELT_INSERT=gl.SQL_MAX_ELT_INSERT,
        TEST_RESTART=test_restart,
        MD=md,
    )


def download(query, out, merge=True, test_restart=False, md=''):
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE=query,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_FILE=out,
        OUT_RG_DIR=gl.SQL_DL_OUT_RG_FOLDER,
        MAX_BDD_CNX=3,
        MERGE_RG_FILES=merge,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
        TEST_RESTART=test_restart,
        MD=md,
    )


def test_sql():
    com.init_log('test_sql', True)
    com.mkdirs(gl.SQL_TMP, True)
    com.mkdirs(gl.SQL_OUT, True)
    com.log_print()

    # com.log('Test sql.execute-----------------------------')
    # execute()

    # com.log('Test sql.upload------------------------------')
    # ttry(upload, g.E_MH, gl.SQL_IN_FILE_MH)
    upload_interrupted()
    upload(gl.SQL_IN_FILE)

    com.log('Test sql.dowload-----------------------------')
    # test download no output
    download(gl.SQL_QUERY_NO, gl.SQL_DL_OUT)

    download(gl.SQL_QUERY, gl.SQL_DL_OUT)
    q.file_match(gl.SQL_IN_FILE, gl.SQL_DL_OUT)
    q.file_match(gl.OUT_DUP_TMP, gl.SQL_OUT_DUP_REF)

    com.log("Test sql.dowload RG avec merge---------------")
    download_interrupted(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG)
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG, test_restart=True)
    q.file_match(gl.SQL_DL_OUT, gl.SQL_DL_OUT_RG)

    com.log("Test sql.dowload RG sans merge---------------")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG, False)
    q.file_match(gl.SQL_RG_REF, gl.SQL_RG_COMP)

    com.log("Test count simple----------------------------")
    download(gl.SQL_QUERY_COUNT_1, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_1_REF)
    download(gl.SQL_QUERY_COUNT_1_RG, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_1_REF)

    com.log("Test count group by--------------------------")
    download(gl.SQL_QUERY_COUNT_2, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_2_REF)
    download(gl.SQL_QUERY_COUNT_2_RG, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_2_REF)


def upload_interrupted():
    manager = Manager()
    md = manager.dict()
    md['T'] = False
    md['LOG_FILE'] = g.LOG_FILE
    p = Process(target=upload, args=(gl.SQL_IN_FILE, True, md))
    p.start()
    while not md['T']:
        pass
    t = md['T'] / 1000
    sleep(t)
    p.terminate()


def download_interrupted(query, out):
    manager = Manager()
    md = manager.dict()
    md['STOP'] = False
    md['N_STOP'] = 0.8 * 2900
    md['LOG_FILE'] = g.LOG_FILE
    p = Process(target=download, args=(query, out, True, True, md))
    p.start()
    while not md['STOP']:
        pass
    p.terminate()


if __name__ == '__main__':
    test_sql()
