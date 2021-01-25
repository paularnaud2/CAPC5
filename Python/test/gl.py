import conf as cfg

# main
TEST_DIR = 'test/'

# test_sql
TEST_SQL_DIR = TEST_DIR + 'sql/'
SQL_ENV = cfg.TEST_ENV
SQL_BDD = cfg.TEST_BDD
SQL_TABLE_NAME = 'TEST'
SQL_CREATE_TABLE = TEST_SQL_DIR + 'create_table_test.sql'
SQL_INSERT_TABLE = TEST_SQL_DIR + 'insert_table_test.sql'
SQL_QUERY = TEST_SQL_DIR + 'e_test.sql'
SQL_QUERY_RG = TEST_SQL_DIR + 'e_test_rg.sql'
SQL_IN_FILE = TEST_SQL_DIR + 'test_sql_in.csv'
SQL_DL_OUT = 'export_test.csv'
SQL_DL_OUT_RG = 'export_test_rg.csv'
SQL_MAX_ELT_INSERT = 200

# test_reqlist
TEST_SQL_DIR = TEST_DIR + 'reqlist/'

# test_qdd
TEST_QDD_DIR = TEST_DIR + 'qdd/'
IN11 = 'qdd_in_test11'
IN12 = 'qdd_in_test12'
REF1 = 'qdd_out_ref_test1.csv'
REF_DUP1 = 'qdd_out_ref_dup_test11.csv'
OUT1 = 'test_qdd_out_1'

IN21 = 'qdd_in_test21'
IN22 = 'qdd_in_test22'
REF2 = 'qdd_out_ref_test2.csv'
REF_DUP2 = 'qdd_out_ref_dup_test22.csv'
OUT2 = 'test_qdd_out_2'

IN31 = 'qdd_in_test31'
IN32 = 'qdd_in_test32'
REF3 = 'qdd_out_ref_test3.csv'
REF_DUP3 = 'qdd_out_ref_dup_test31.csv'
OUT3 = 'test_qdd_out_3'
