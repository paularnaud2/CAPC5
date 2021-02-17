import qdd as q
import common as com

from test import gl
from toolParseXML import parse_xml
from toolSplit import split_file
from toolDup import find_dup
from toolDup import find_dup_col


def split():
    split_file(
        IN_DIR=gl.SQL_IN_FILE,
        OUT_DIR=gl.TOOLS_OUT,
        MAX_LINE=1000,
        MAX_FILE_NB=3,
        ADD_HEADER=True,
    )
    q.file_match(gl.S_OUT_1, gl.S_OUT_REF_1)
    q.file_match(gl.S_OUT_2, gl.S_OUT_REF_2)
    q.file_match(gl.S_OUT_3, gl.S_OUT_REF_3)


def test_tools():
    com.init_log('test_tools', True)
    com.mkdirs(gl.TOOLS_OUT, True)
    com.log_print()

    parse_xml(IN_DIR=gl.XML_IN, OUT_DIR=gl.XML_OUT)
    q.file_match(gl.XML_OUT, gl.XML_OUT_REF)

    split()

    find_dup(gl.DUP_IN, gl.DUP_OUT)
    q.file_match(gl.DUP_OUT, gl.DUP_OUT_REF)

    find_dup_col(gl.DUP_COL_IN)
    q.file_match(gl.DUP_OUT, gl.DUP_OUT_REF)


if __name__ == '__main__':
    test_tools()
