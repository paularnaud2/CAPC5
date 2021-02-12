import common as com
import reqlist as rl
import qdd as q

from test import gl
from test_sql import upload
from test_sql import execute


def reqlist(in_file, out_file, query_file):
    rl.run_reqList(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE=query_file,
        IN_FILE=in_file,
        OUT_FILE=out_file,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        MAX_BDD_CNX=4,
        NB_MAX_ELT_IN_STATEMENT=100,
        SL_STEP_QUERY=5,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


def left_join(left, right, ref):
    rl.left_join(left, right, gl.RL_OUT_JOIN, debug=False)
    q.file_match(ref, gl.RL_OUT_JOIN, gl.FM)


def test_reqlist():
    com.init_log('test_reqlist', True)
    com.mkdirs(gl.RL_OUT_DIR, True)
    left_join(gl.RL_LEFT_1, gl.RL_RIGHT_1, gl.RL_OUT_JOIN_REF_1)
    left_join(gl.RL_LEFT_2, gl.RL_RIGHT_2, gl.RL_OUT_JOIN_REF_2)
    left_join(gl.RL_LEFT_3, gl.RL_RIGHT_3, gl.RL_OUT_JOIN_REF_3)
    execute()
    upload()
    arr = com.load_csv(gl.SQL_IN_FILE)
    arr = [elt[0] for elt in arr]
    com.save_csv(arr, gl.RL_IN_1)
    com.log('Test reqlist')
    reqlist(gl.RL_IN_1, gl.RL_OUT_1, gl.RL_QUERY_1)
    reqlist(gl.RL_OUT_1, gl.RL_OUT_2, gl.RL_QUERY_2)
    q.file_match(gl.SQL_IN_FILE, gl.RL_OUT_2, gl.FM)


if __name__ == '__main__':
    test_reqlist()
