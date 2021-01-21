import qdd as q
import common as com
import qdd.gl as qgl

from common import g
from test import gl


def init():
    gl.TMP_DIR = g.paths['TMP'] + gl.TEST_QDD_DIR
    com.mkdirs(gl.TMP_DIR, True)


def qdd(in1, in2, out, ref, mrl, ref_dup='', dup_nb=1):
    q.run_qdd(
        IN_DIR=gl.TEST_QDD_DIR,
        IN_FILE_NAME_1=in1,
        IN_FILE_NAME_2=in2,
        OUT_DIR=gl.TMP_DIR,
        OUT_FILE_NAME=out,
        MAX_ROW_LIST=mrl,
        EQUAL_OUT=False,
        DIFF_OUT=False,
        OPEN_OUT_FILE=False,
    )
    left = gl.TEST_QDD_DIR + ref
    right = gl.TMP_DIR + out + qgl.FILE_TYPE
    q.file_match(left, right)
    if ref_dup:
        left = gl.TEST_QDD_DIR + ref_dup
        right = f'{qgl.OUT_DUP_FILE}{dup_nb}{qgl.FILE_TYPE}'
        q.file_match(left, right)


def test_qdd():
    com.init_log('test_qdd', True)
    init()
    qdd(gl.IN11, gl.IN12, gl.OUT1, gl.REF1, 100, gl.REF_DUP1)
    qdd(gl.IN11, gl.IN12, gl.OUT1, gl.REF1, 15, gl.REF_DUP1)
    qdd(gl.IN21, gl.IN22, gl.OUT2, gl.REF2, 100, gl.REF_DUP2, 2)
    qdd(gl.IN21, gl.IN22, gl.OUT2, gl.REF2, 15, gl.REF_DUP2, 2)
    qdd(gl.IN31, gl.IN32, gl.OUT3, gl.REF3, 100)
    qdd(gl.IN31, gl.IN32, gl.OUT3, gl.REF3, 15)


if __name__ == '__main__':
    test_qdd()
