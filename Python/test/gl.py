from common import g
import conf as cfg

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
SQL_MAX_ELT_INSERT = 200

# test_reqlist
TEST_RL_DIR = TEST_DIR + 'reqlist/'
RL_OUT = g.paths['TMP'] + TEST_RL_DIR
RL_LEFT = TEST_RL_DIR + 'left.csv'
RL_RIGHT = TEST_RL_DIR + 'right.csv'
RL_QUERY = TEST_RL_DIR + 'query.sql'
RL_OUT_JOIN = RL_OUT + 'join.csv'
RL_OUT_JOIN_REF = TEST_RL_DIR + 'join_ref.csv'

# test_qdd
TEST_QDD_DIR = TEST_DIR + 'qdd/'
QDD_OUT = g.paths['TMP'] + TEST_QDD_DIR
FILE_MATCH_OUT = QDD_OUT + 'file_match.csv'
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
