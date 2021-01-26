import common as com
import reqlist as rl

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
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        NB_MAX_ELT_IN_STATEMENT=500,
        SL_STEP_QUERY=50,
    )


def test_reqlist():
    com.init_log('test_reqlist', True)
    com.mkdirs(gl.RL_OUT, True)
    rl.join(gl.RL_LEFT, gl.RL_RIGHT, gl.RL_OUT_JOIN)
    # execute()
    # upload()
    # com.log('Test reqlist')
    # reqlist(gl.RL_OUT)


if __name__ == '__main__':
    test_reqlist()
