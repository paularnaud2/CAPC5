import SQL as sql

if __name__ == '__main__':
    sql.download(
        MAX_BDD_CNX=10,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
    )

    # table_name = 'TEST_AFF'
    # sql.execute(
    #     SCRIPT_FILE='SQL/procs/create_table_aff.sql',
    #     VAR_DICT={'@@TABLE_NAME@@': table_name},
    #     PROC=True,
    #     ENV='DIRECT',
    #     BDD='CAPC5',
    # )

    # sql.upload(
    #     SCRIPT_FILE='SQL/scripts/insert_table_aff.sql',
    #     IN_DIR='C:/Py/OUT/test.csv',
    #     VAR_DICT={'@@TABLE_NAME@@': table_name},
    #     NB_MAX_ELT_INSERT=100,
    #     ENV='DIRECT',
    #     BDD='CAPC5',
    # )
