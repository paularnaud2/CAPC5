import time
import sql
import common as com

from datetime import datetime
from reqlist import run_reqList


def run_sge(test=False):
    # Définition des variables
    start_time = time.time()
    date = datetime.now().strftime("%Y%m%d")
    in_file = 'C:/Py/IN/perimetre_fin_trv.csv'
    out_file = f'C:/Py/OUT/out_SGE_FULL_FIN_TRV_{date}.csv'
    tmp_table = 'SGE_FULL_TMP'
    final_table = f'SGE_FULL_{date}'
    view_name = 'SGE'
    max_elt_insert = 10000
    max_elt_st = 500
    max_db_cnx = 8
    sl_step_query = 100

    if test:
        in_file = 'C:/Py/IN/perimetre_fin_trv_test.csv'
        out_file = f'C:/Py/OUT/out_test_SGE_{date}.csv'
        tmp_table = 'SGE_TEST_TMP'
        final_table = f'SGE_TEST_{date}'
        view_name = 'SGE_TEST'
        max_elt_insert = 100
        max_elt_st = 10
        max_db_cnx = 6
        sl_step_query = 10

    squeeze_downl = False
    squeeze_upl = False

    com.log("Lancement du job " + __name__)
    if not squeeze_downl:
        com.log('Export SGE\
------------------------------------------------------------')
        run_reqList(
            ENV='PROD',
            DB='SGE',
            QUERY_FILE='reqlist/queries/SGE_SUIVI_FIN_TRV.sql',
            IN_FILE=in_file,
            OUT_FILE=out_file,
            MAX_DB_CNX=max_db_cnx,
            SL_STEP_QUERY=sl_step_query,
            NB_MAX_ELT_IN_STATEMENT=max_elt_st,
            OPEN_OUT_FILE=False,
            SQUEEZE_JOIN=True,
            SQUEEZE_SQL=False,
            CHECK_DUP=False,
            SEND_NOTIF=False,
        )

    com.log(f'Création de la table temporaire {tmp_table}\
------------------------------------')
    sql.execute(
        ENV='DIRECT',
        DB='CAPC5',
        SCRIPT_FILE='sql/procs/create_table_sge_tmp.sql',
        VAR_DICT={'TABLE_NAME': tmp_table},
        PROC=True,
    )

    if not squeeze_upl:
        com.log('Export des données importées dans la table temporaire créée\
----------------------')
        sql.upload(
            ENV='DIRECT',
            DB='CAPC5',
            SCRIPT_FILE='sql/scripts/insert_table_sge.sql',
            VAR_DICT={'TABLE_NAME': tmp_table},
            UPLOAD_IN=out_file,
            NB_MAX_ELT_INSERT=max_elt_insert,
        )

    com.log(f'Création de la table finale {final_table}\
------------------------------------')
    sql.execute(
        ENV='DIRECT',
        DB='CAPC5',
        SCRIPT_FILE='sql/procs/create_table_sge_final.sql',
        VAR_DICT={'TABLE_NAME': final_table},
        PROC=True,
    )

    com.log('Copie de la table temporaire dans la table finale\
--------------------')
    sql.execute(
        ENV='DIRECT',
        DB='CAPC5',
        SCRIPT_FILE='sql/scripts/from_tmp_to_final.sql',
        VAR_DICT={
            'TMP_TABLE': tmp_table,
            'FINAL_TABLE': final_table,
        },
    )

    com.log(f'Mise à jour de la vue {view_name}\
-----------------------------------')
    sql.execute(
        ENV='DIRECT',
        DB='CAPC5',
        SCRIPT_FILE='sql/scripts/update_view_sge.sql',
        VAR_DICT={
            'TABLE_NAME': final_table,
            'VIEW_NAME': view_name,
        },
    )

    dur = com.get_duration_ms(start_time)
    sd = com.get_duration_string(dur)
    s = f"Job {__name__} terminé en {sd}."
    com.log(s)
    com.log_print()
    com.send_notif(s, __name__, dur)
