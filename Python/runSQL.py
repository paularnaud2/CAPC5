from SQL import export, execute, sql_import

if __name__ == '__main__':
    export(
        MAX_BDD_CNX=10,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
    )

    # table_name = 'TEST_AFF_2'
    # execute(SCRIPT_FILE='SQL/procs/create_table_aff.sql',
    #         VAR_VALUE=table_name,
    #         VAR_NAME='@@TABLE_NAME@@',
    #         PROC=True,
    #         ENV='DIRECT',
    #         BDD='CAPC5')

    # sql_import(IN_DIR='C:/Py/OUT/test.csv',
    #            TABLE_NAME='TEST_PYTHON',
    #            NB_MAX_ELT_INSERT=50000,
    #            ENV='DIRECT',
    #            BDD='CAPC5',
    #            QUERY_FILE='SQL/scripts/insert_table_aff.sql')
