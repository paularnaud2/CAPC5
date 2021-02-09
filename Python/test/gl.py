from common import g
import conf_main as cfg

# main
TEST_DIR = 'test/'

# test_sql
TEST_SQL_DIR = TEST_DIR + 'sql/'
SQL_ENV = cfg.TEST_ENV
SQL_BDD = cfg.TEST_BDD
SQL_TABLE_NAME = 'TEST'
SQL_CREATE_TABLE = TEST_SQL_DIR + 'create_table.sql'
SQL_INSERT_TABLE = TEST_SQL_DIR + 'insert_table.sql'
SQL_QUERY = TEST_SQL_DIR + 'export.sql'
SQL_QUERY_RG = TEST_SQL_DIR + 'export_rg.sql'
SQL_IN_FILE = TEST_SQL_DIR + 'in.csv'
SQL_OUT = g.paths['TMP'] + TEST_SQL_DIR
SQL_DL_OUT = SQL_OUT + 'sql_test_out.csv'
SQL_DL_OUT_RG = SQL_OUT + 'sql_test_out_rg.csv'
SQL_DL_OUT_RG_FOLDER = SQL_OUT + 'RG_TEST/'
SQL_RG_REF = TEST_SQL_DIR + '01_ref.csv'
SQL_RG_COMP = SQL_DL_OUT_RG_FOLDER + '01.csv'
SQL_MAX_ELT_INSERT = 200

# test_reqlist
TEST_RL_DIR = TEST_DIR + 'reqlist/'
RL_OUT_DIR = g.paths['TMP'] + TEST_RL_DIR
RL_OUT_JOIN = RL_OUT_DIR + 'join.csv'

RL_IN_1 = RL_OUT_DIR + 'in1.csv'
RL_OUT_1 = RL_OUT_DIR + 'out1.csv'
RL_QUERY_1 = TEST_RL_DIR + 'query1.sql'
RL_IN_2 = RL_OUT_DIR + 'in2.csv'
RL_OUT_2 = RL_OUT_DIR + 'out2.csv'
RL_QUERY_2 = TEST_RL_DIR + 'query2.sql'

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
FILE_MATCH_OUT = g.paths['TMP'] + TEST_DIR + 'file_match.csv'
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
REF_DUP3 = 'out_ref_dup_31.csv'
OUT3 = '3'

# test tools
TOOLS_OUT = g.paths['TMP'] + 'tools/'

# test XML
XML_IN = 'test/tools/in.xml'
XML_OUT = TOOLS_OUT + 'out.csv'
XML_OUT_REF = 'test/tools/out_ref.csv'

# test split
S_OUT = TOOLS_OUT + 'out_2.csv'
S_OUT_REF = 'test/tools/out_2_ref.csv'
