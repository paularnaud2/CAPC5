import sql
import qdd as q
import common as com

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
        OUT_FILE=out,
        OUT_RG_DIR=gl.SQL_DL_OUT_RG_FOLDER,
        MAX_BDD_CNX=8,
        MERGE_RG_FILES=merge,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


def test_sql():
    com.init_log('test_sql', True)
    com.mkdirs(gl.SQL_OUT, True)
    execute()
    upload()
    download(gl.SQL_QUERY, gl.SQL_DL_OUT)
    com.log("Téléchargement des données par plages avec merge")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG)
    com.log("Téléchargement des données par plages sans merge")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG, False)

    q.file_match(gl.SQL_DL_OUT, gl.SQL_DL_OUT_RG)
    q.file_match(gl.SQL_RG_REF, gl.SQL_RG_COMP)


if __name__ == '__main__':
    test_sql()
