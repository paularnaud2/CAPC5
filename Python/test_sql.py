import sql
import common as com

from common import g
from test import gl

com.init_log('test_sql')


def execute():
    com.log(f'Création de la table {gl.SQL_TABLE_NAME}\
    (test sql.execute)-------------------------------')
    sql.execute(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE='sql/procs/create_table_test.sql',
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        PROC=True,
    )
    com.log_print('')


def upload():
    com.log('Export des données (test sql.upload)\
----------------------')
    sql.upload(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE='sql/scripts/insert_table_test.sql',
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        UPLOAD_IN=gl.SQL_IN_FILE,
        NB_MAX_ELT_INSERT=gl.SQL_MAX_ELT_INSERT,
    )
    com.log_print('')


def download_simple():
    com.log('Téléchargement des données (test sql.download)\
----------------------')
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE='sql/queries/e_test.sql',
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_FILE=g.paths['OUT'] + gl.SQL_DL_OUT,
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )
    com.log_print('')


def download_rg_merge():
    com.log(
        'Téléchargement des données par plages avec merge (test sql.download)\
----------------------')
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE='sql/queries/e_test_rg.sql',
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_FILE=g.paths['OUT'] + gl.SQL_DL_RG_OUT,
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


def download_rg_no_merge():
    com.log(
        'Téléchargement des données par plages sans merge (test sql.download)\
----------------------')
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE='sql/queries/e_test_rg.sql',
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_RG_DIR=g.paths['OUT'] + 'RG_TEST/',
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=False,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
    )
    com.log_print('')


def compare():
    com.log(f'Comparaison des fichiers {gl.SQL_DL_OUT} et {gl.SQL_DL_RG_OUT}')


def test_sql():
    execute()
    upload()
    download_simple()
    download_rg_merge()
    download_rg_no_merge()
    compare()


if __name__ == '__main__':
    test_sql()
