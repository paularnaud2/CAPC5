import common as com
import reqlist as rl
import qdd as q

from test import gl
from test_sql import upload
from test_sql import execute
from test_sql import download


def reqlist(out, in_file):

    rl.run_reqList(
        QUERY_FILE=gl.RL_QUERY,
        # IN_FILE=g.paths['OUT'] + in_file,
        # OUT_FILE=g.paths['OUT'] + out,
        MAX_BDD_CNX=8,
        NB_MAX_ELT_IN_STATEMENT=500,
        SL_STEP_QUERY=50,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
    )


def left_join(left, right, ref):
    rl.left_join(left, right, gl.RL_OUT_JOIN, debug=False)
    q.file_match(ref, gl.RL_OUT_JOIN, gl.FILE_MATCH_OUT)


def test_reqlist():
    com.init_log('test_reqlist', True)
    com.mkdirs(gl.RL_OUT, True)
    left_join(gl.RL_LEFT_1, gl.RL_RIGHT_1, gl.RL_OUT_JOIN_REF_1)
    left_join(gl.RL_LEFT_2, gl.RL_RIGHT_2, gl.RL_OUT_JOIN_REF_2)
    left_join(gl.RL_LEFT_3, gl.RL_RIGHT_3, gl.RL_OUT_JOIN_REF_3)
    # execute()
    # upload()
    # com.log('Test reqlist')
    # reqlist(gl.RL_OUT)


if __name__ == '__main__':
    test_reqlist()
