import sql
import common as com

from common import g
from test import gl


def execute():
    com.log('Test sql.execute)----------------------')
    sql.execute(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_CREATE_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        PROC=True,
    )


def upload():
    com.log('Test sql.upload)----------------------')
    sql.upload(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_INSERT_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        UPLOAD_IN=gl.SQL_IN_FILE,
        NB_MAX_ELT_INSERT=gl.SQL_MAX_ELT_INSERT,
    )


def download(query, out, merge=True):
    com.log('Test sql.download)----------------------')
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE=query,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_FILE=g.paths['OUT'] + out,
        OUT_RG_DIR=g.paths['OUT'] + 'RG_TEST/',
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=merge,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


def compare():
    com.log(f'Comparaison des fichiers {gl.SQL_DL_OUT} et {gl.SQL_DL_OUT_RG}')


def test_sql():
    com.init_log('test_sql', True)
    execute()
    upload()
    download(gl.SQL_QUERY, gl.SQL_DL_OUT)
    com.log("Téléchargement des données par plages avec merge")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG)
    com.log("Téléchargement des données par plages sans merge")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG, False)
    compare()


if __name__ == '__main__':
    test_sql()
