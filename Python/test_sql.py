import common as com
from common import g
com.init_log('test_sql')


def test_sql():
    import sql

    env = 'DIRECT'
    bdd = 'CAPC5'
    table_name = 'TEST'
    in_file = 'test/test_sql_in.csv'
    max_elt_insert = 200

    com.log(f'Création de la table {table_name}\
 (test execute)-------------------------------')
    sql.execute(
        ENV=env,
        BDD=bdd,
        SCRIPT_FILE='sql/procs/create_table_test.sql',
        VAR_DICT={'@@TABLE_NAME@@': table_name},
        PROC=True,
    )
    com.log_print('')
    com.log('Export des données (test upload)\
----------------------')
    sql.upload(
        ENV=env,
        BDD=bdd,
        SCRIPT_FILE='sql/scripts/insert_table_test.sql',
        VAR_DICT={'@@TABLE_NAME@@': table_name},
        IN_DIR=in_file,
        NB_MAX_ELT_INSERT=max_elt_insert,
    )
    com.log_print('')
    com.log('Téléchargement des données (test sql.download)\
----------------------')
    sql.download(
        ENV=env,
        BDD=bdd,
        QUERY_FILE='sql/queries/e_test.sql',
        OUT_DIR=g.paths['OUT'],
        OUT_RG_FOLDER=g.paths['OUT'] + 'RG_TEST',
        OUT_FILE=g.paths['OUT'] + 'export_test.csv',
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )

    com.log_print('')
    com.log(
        'Téléchargement des données par plages sans merge (test sql.download)\
----------------------')
    sql.download(
        ENV=env,
        BDD=bdd,
        QUERY_FILE='sql/queries/e_test_rg.sql',
        OUT_DIR=g.paths['OUT'],
        OUT_RG_FOLDER='RG_TEST',
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=False,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
    )

    com.log_print('')
    com.log(
        'Téléchargement des données par plages avec merge (test sql.download)\
----------------------')
    sql.download(
        ENV=env,
        BDD=bdd,
        QUERY_FILE='sql/queries/e_test_rg.sql',
        OUT_DIR=g.paths['OUT'],
        OUT_RG_FOLDER='RG_TEST',
        OUT_FILE=g.paths['OUT'] + 'export_test_rg.csv',
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


if __name__ == '__main__':
    test_sql()
