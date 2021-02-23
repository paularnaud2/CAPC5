import sql
import qdd as q
import common as com

from test import gl


def execute():
    sql.execute(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_CREATE_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        PROC=True,
    )


def upload():
    sql.upload(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        SCRIPT_FILE=gl.SQL_INSERT_TABLE,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        UPLOAD_IN=gl.SQL_IN_FILE,
        NB_MAX_ELT_INSERT=gl.SQL_MAX_ELT_INSERT,
    )


def download(query, out, merge=True):
    sql.download(
        ENV=gl.SQL_ENV,
        BDD=gl.SQL_BDD,
        QUERY_FILE=query,
        VAR_DICT={'TABLE_NAME': gl.SQL_TABLE_NAME},
        OUT_FILE=out,
        OUT_RG_DIR=gl.SQL_DL_OUT_RG_FOLDER,
        MAX_BDD_CNX=3,
        MERGE_RG_FILES=merge,
        EXPORT_RANGE=False,
        CHECK_DUP=True,
        OPEN_OUT_FILE=False,
    )


def test_sql():
    # com.init_log('test_sql', True)
    # com.mkdirs(gl.SQL_OUT, True)
    # com.log_print()

    com.log('Test sql.execute-----------------------------')
    execute()

    com.log('Test sql.upload------------------------------')
    upload()

    com.log('Test sql.dowload-----------------------------')
    download(gl.SQL_QUERY, gl.SQL_DL_OUT)
    q.file_match(gl.SQL_IN_FILE, gl.SQL_DL_OUT)
    q.file_match(gl.OUT_DUP_TMP, gl.SQL_OUT_DUP_REF)

    com.log("Test sql.dowload RG avec merge---------------")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG)
    q.file_match(gl.SQL_DL_OUT, gl.SQL_DL_OUT_RG)

    com.log("Test sql.dowload RG sans merge---------------")
    download(gl.SQL_QUERY_RG, gl.SQL_DL_OUT_RG, False)
    q.file_match(gl.SQL_RG_REF, gl.SQL_RG_COMP)

    com.log("Test count simple----------------------------")
    download(gl.SQL_QUERY_COUNT_1, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_1_REF)
    download(gl.SQL_QUERY_COUNT_1_RG, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_1_REF)

    com.log("Test count group by--------------------------")
    download(gl.SQL_QUERY_COUNT_2, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_2_REF)
    download(gl.SQL_QUERY_COUNT_2_RG, gl.SQL_DL_OUT_COUNT)
    q.file_match(gl.SQL_DL_OUT_COUNT, gl.SQL_DL_OUT_COUNT_2_REF)


if __name__ == '__main__':
    test_sql()
