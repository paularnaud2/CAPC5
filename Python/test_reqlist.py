import common as com
import reqlist as rl
import qdd as q

from common import g
from test import gl
from test_sql import upload
from test_sql import execute

from time import sleep
from multiprocessing import Process
from multiprocessing import Manager


def reqlist(in_file, out_file, query_file, test_restart=False, md=''):
    rl.run_reqList(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE=query_file,
        IN_FILE=in_file,
        OUT_FILE=out_file,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        MAX_BDD_CNX=3,
        NB_MAX_ELT_IN_STATEMENT=100,
        SL_STEP_QUERY=5,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
        TEST_RESTART=test_restart,
        MD=md,
    )


def left_join(left, right, ref):
    rl.left_join(left, right, gl.RL_OUT_JOIN, debug=False)
    q.file_match(ref, gl.RL_OUT_JOIN)


def test_reqlist():
    com.init_log('test_reqlist', True)
    com.mkdirs(gl.RL_TMP_DIR, True)
    com.mkdirs(gl.RL_OUT_DIR, True)
    com.log_print()
    com.log('Test join----------------------------------------')
    left_join(gl.RL_LEFT_1, gl.RL_RIGHT_1, gl.RL_OUT_JOIN_REF_1)
    left_join(gl.RL_LEFT_2, gl.RL_RIGHT_2, gl.RL_OUT_JOIN_REF_2)
    left_join(gl.RL_LEFT_3, gl.RL_RIGHT_3, gl.RL_OUT_JOIN_REF_3)

    com.log("Préparation de la BDD----------------------------")
    execute()
    upload()
    arr = com.load_csv(gl.SQL_IN_FILE)
    arr = [elt[0] for elt in arr]
    com.save_csv(arr, gl.RL_IN_1)

    com.log('Test reqlist--------------------------------------')
    reqlist(gl.RL_IN_1, gl.RL_OUT_1, gl.RL_QUERY_1)
    reqlist(gl.RL_OUT_1, gl.RL_OUT_2, gl.RL_QUERY_2)
    q.file_match(gl.SQL_IN_FILE, gl.RL_OUT_2, del_dup=True)
    q.file_match(gl.OUT_DUP_TMP, gl.RL_OUT_DUP_REF)

    reqlist_interrupted(gl.RL_OUT_1, gl.RL_OUT_3, gl.RL_QUERY_2)
    reqlist(gl.RL_OUT_1, gl.RL_OUT_3, gl.RL_QUERY_2, True)
    q.file_match(gl.RL_OUT_2, gl.RL_OUT_3)


def reqlist_interrupted(inp, out, query):
    manager = Manager()
    md = manager.dict()
    md['STOP'] = False
    md['LOG_FILE'] = g.LOG_FILE
    p = Process(target=reqlist, args=(inp, out, query, True, md))
    p.start()
    while not md['STOP']:
        sleep(0.1)
    p.terminate()


if __name__ == '__main__':
    test_reqlist()
