import qdd
import common as com
import qdd.gl as qgl

from common import g
from test import gl


def test_qdd():
    com.init_log('test_qdd', True)
    qdd.run_qdd(
        IN_DIR=gl.TEST_DIR,
        IN_FILE_NAME_1=gl.IN11,
        IN_FILE_NAME_2=gl.IN12,
        OUT_DIR=g.paths['OUT'],
        OUT_FILE_NAME=gl.OUT1,
        MAX_ROW_LIST=15,
        MAX_LINE_SPLIT=100,
        EQUAL_OUT=False,
        DIFF_OUT=False,
        OPEN_OUT_FILE=False,
    )
    left = gl.TEST_DIR + gl.REF1
    right = g.paths['OUT'] + gl.OUT1 + qgl.FILE_TYPE
    qdd.file_match(left, right)


if __name__ == '__main__':
    test_qdd()
