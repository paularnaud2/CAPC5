from SQL import export, sql_import

#export()

sql_import(IN_DIR = 'C:/Py/OUT/test.csv', TABLE_NAME = 'TEST_PYTHON', NB_MAX_ELT_INSERT = 50000, ENV = 'DIRECT', BDD = 'CAPC5', QUERY_FILE = 'SQL/scripts/insert_table_aff.sql')
