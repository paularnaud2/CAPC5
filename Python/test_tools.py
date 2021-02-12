import qdd as q
import common as com

from test import gl
from toolParseXML import parse_xml
from toolSplit import split_file
from toolDup import find_dup_main


def test_tools():
    com.init_log('test_tools', True)
    com.mkdirs(gl.TOOLS_OUT, True)
    com.log_print()
    parse_xml(gl.XML_IN, gl.XML_OUT)
    q.file_match(gl.XML_OUT, gl.XML_OUT_REF, gl.FM)
    split_file(gl.XML_OUT, max_line=2)
    q.file_match(gl.S_OUT, gl.S_OUT_REF, gl.FM)

    find_dup_main(gl.DUP_IN, gl.DUP_OUT)
    q.file_match(gl.DUP_OUT, gl.DUP_OUT_REF, gl.FM)


if __name__ == '__main__':
    test_tools()
