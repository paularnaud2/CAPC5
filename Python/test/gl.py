import toolDup
import conf_main as cfg
import tools.gl as tools
import reqlist.gl as rl

from common import g

# main
TEST_DIR = 'test/'
OUT_DUP_TMP = g.paths['TMP'] + tools.TMP_FOLDER + toolDup.TMP_OUT

# test_sql
TEST_SQL_DIR = TEST_DIR + 'sql/'
SQL_ENV = cfg.TEST_ENV
SQL_BDD = cfg.TEST_BDD
SQL_TABLE_NAME = 'TEST'
SQL_CREATE_TABLE = TEST_SQL_DIR + 'create_table.sql'
SQL_INSERT_TABLE = TEST_SQL_DIR + 'insert_table.sql'
SQL_QUERY = TEST_SQL_DIR + 'export.sql'
SQL_QUERY_RG = TEST_SQL_DIR + 'export_rg.sql'
SQL_QUERY_COUNT_1 = TEST_SQL_DIR + 'count_1.sql'
SQL_QUERY_COUNT_1_RG = TEST_SQL_DIR + 'count_1_rg.sql'
SQL_QUERY_COUNT_2 = TEST_SQL_DIR + 'count_2.sql'
SQL_QUERY_COUNT_2_RG = TEST_SQL_DIR + 'count_2_rg.sql'
SQL_IN_FILE = TEST_SQL_DIR + 'in.csv'
SQL_OUT = g.paths['TMP'] + TEST_SQL_DIR
SQL_OUT_DUP_REF = TEST_SQL_DIR + 'out_dup_ref.csv'
SQL_DL_OUT = SQL_OUT + 'out.csv'
SQL_DL_OUT_COUNT = SQL_OUT + 'out_count.csv'
SQL_DL_OUT_COUNT_1_REF = TEST_SQL_DIR + 'out_count_1_ref.csv'
SQL_DL_OUT_COUNT_2_REF = TEST_SQL_DIR + 'out_count_2_ref.csv'
SQL_DL_OUT_RG = SQL_OUT + 'out_rg.csv'
SQL_DL_OUT_RG_FOLDER = SQL_OUT + 'RG_TEST/'
SQL_RG_REF = TEST_SQL_DIR + '01_ref.csv'
SQL_RG_COMP = SQL_DL_OUT_RG_FOLDER + '01.csv'
SQL_MAX_ELT_INSERT = 200

# test_reqlist
TEST_RL_DIR = TEST_DIR + 'reqlist/'
RL_OUT_DIR = g.paths['TMP'] + TEST_RL_DIR
RL_TMP_DIR = g.paths['TMP'] + rl.TMP_FOLDER
RL_OUT_JOIN = RL_OUT_DIR + 'join.csv'
RL_OUT_DUP_REF = TEST_RL_DIR + 'out_dup_ref.csv'

RL_IN_1 = RL_OUT_DIR + 'in1.csv'
RL_OUT_1 = RL_OUT_DIR + 'out1.csv'
RL_QUERY_1 = TEST_RL_DIR + 'query1.sql'
RL_IN_2 = RL_OUT_DIR + 'in2.csv'
RL_OUT_2 = RL_OUT_DIR + 'out2.csv'
RL_QUERY_2 = TEST_RL_DIR + 'query2.sql'
RL_OUT_3 = RL_OUT_DIR + 'out3.csv'

RL_LEFT_1 = TEST_RL_DIR + 'left_1.csv'
RL_RIGHT_1 = TEST_RL_DIR + 'right_1.csv'
RL_OUT_JOIN_REF_1 = TEST_RL_DIR + 'join_ref_1.csv'

RL_LEFT_2 = TEST_RL_DIR + 'left_2.csv'
RL_RIGHT_2 = TEST_RL_DIR + 'right_2.csv'
RL_OUT_JOIN_REF_2 = TEST_RL_DIR + 'join_ref_2.csv'

RL_LEFT_3 = TEST_RL_DIR + 'left_3.csv'
RL_RIGHT_3 = TEST_RL_DIR + 'right_3.csv'
RL_OUT_JOIN_REF_3 = TEST_RL_DIR + 'join_ref_3.csv'

# test_qdd
TEST_QDD_DIR = TEST_DIR + 'qdd/'
QDD_OUT = g.paths['TMP'] + TEST_QDD_DIR
FM = g.paths['TMP'] + TEST_DIR + 'file_match_out.csv'
IN11 = 'in_11'
IN12 = 'in_12'
REF1 = 'out_ref_1.csv'
REF_DUP1 = 'out_ref_dup_11.csv'
OUT1 = '1'

IN21 = 'in_21'
IN22 = 'in_22'
REF2 = 'out_ref_2.csv'
REF_DUP2 = 'out_ref_dup_22.csv'
OUT2 = '2'

IN31 = 'in_31'
IN32 = 'in_32'
REF3 = 'out_ref_3.csv'
REF_SPLIT_3 = 'out_ref_split_3.csv'
REF_DUP3 = 'out_ref_dup_31.csv'
OUT3 = '3'
OUT_SPLIT_3 = '3_3'

# test tools
TEST_TOOL_DIR = TEST_DIR + tools.TMP_FOLDER
TOOLS_OUT = g.paths['TMP'] + TEST_TOOL_DIR

# test XML
XML_IN = TEST_TOOL_DIR + 'xml_in.xml'
XML_OUT = TOOLS_OUT + 'out_xml.csv'
XML_OUT_REF = TEST_TOOL_DIR + 'xml_out_ref.csv'

# test split
S_OUT_1 = TOOLS_OUT + 'in_1.csv'
S_OUT_2 = TOOLS_OUT + 'in_2.csv'
S_OUT_3 = TOOLS_OUT + 'in_3.csv'
S_OUT_REF_1 = TEST_TOOL_DIR + 'split_out_ref_1.csv'
S_OUT_REF_2 = TEST_TOOL_DIR + 'split_out_ref_2.csv'
S_OUT_REF_3 = TEST_TOOL_DIR + 'split_out_ref_3.csv'

# test dup
DUP_IN = TEST_TOOL_DIR + 'dup_in.csv'
DUP_OUT = TOOLS_OUT + 'out_dup.csv'
DUP_OUT_REF = TEST_TOOL_DIR + 'dup_out_ref.csv'
DEL_DUP_OUT_REF = TEST_TOOL_DIR + 'del_dup_out_ref.csv'
DUP_COL_IN = TEST_TOOL_DIR + 'dup_col_in.csv'
DUP_COL_REF = TEST_TOOL_DIR + 'dup_out_ref_2.csv'
