import time
import SQL as sql
import common as com

from datetime import datetime
from ReqList import run_reqList


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
    sl_step_query = 50

    if test:
        in_file = 'C:/Py/IN/in_test.csv'
        out_file = f'C:/Py/OUT/out_test_SGE_{date}.csv'
        tmp_table = 'SGE_TEST_TMP'
        final_table = f'SGE_TEST_{date}'
        view_name = 'SGE_TEST'
        max_elt_insert = 100

    squeeze_downl = False
    squeeze_upl = False
    (squeeze_downl, squeeze_create_table) = sql.check_restart(squeeze_downl)

    com.log("Lancement du job " + __name__)
    if not squeeze_downl:
        com.log('Export SGE\
------------------------------------------------------------')
        run_reqList(
            ENV='PROD',
            BDD='SGE',
            QUERY_FILE='ReqList/queries/SGE_SUIVI_FIN_TRV.sql',
            IN_FILE=in_file,
            OUT_FILE=out_file,
            MAX_BDD_CNX=8,
            SL_STEP_QUERY=sl_step_query,
            OPEN_OUT_FILE=False,
            SQUEEZE_JOIN=True,
            SQUEEZE_SQL=False,
            CHECK_DUP=False,
            SEND_NOTIF=False,
        )

    if not squeeze_create_table and not squeeze_upl:
        com.log(f'Création de la table temporaire {tmp_table}\
------------------------------------')
        sql.execute(
            ENV='DIRECT',
            BDD='CAPC5',
            SCRIPT_FILE='SQL/procs/create_table_sge_tmp.sql',
            VAR_DICT={'@@TABLE_NAME@@': tmp_table},
            PROC=True,
        )

    if not squeeze_upl:
        com.log_print('')
        com.log('Export des données importées dans la table temporaire créée\
----------------------')
        sql.upload(
            ENV='DIRECT',
            BDD='CAPC5',
            SCRIPT_FILE='SQL/scripts/insert_table_sge.sql',
            VAR_DICT={'@@TABLE_NAME@@': tmp_table},
            IN_DIR=out_file,
            NB_MAX_ELT_INSERT=max_elt_insert,
        )

    com.log_print('')
    com.log(f'Création de la table finale {final_table}\
------------------------------------')
    sql.execute(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='SQL/procs/create_table_sge_final.sql',
        VAR_DICT={'@@TABLE_NAME@@': final_table},
        PROC=True,
    )

    com.log_print('')
    com.log('Copie de la table temporaire dans la table finale\
--------------------')
    sql.execute(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='SQL/scripts/from_tmp_to_final.sql',
        VAR_DICT={
            '@@TMP_TABLE@@': tmp_table,
            '@@FINAL_TABLE@@': final_table,
        },
    )

    com.log_print('')
    com.log(f'Mise à jour de la vue {view_name}\
-----------------------------------')
    sql.execute(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='SQL/scripts/update_view_sge.sql',
        VAR_DICT={
            '@@TABLE_NAME@@': final_table,
            '@@VIEW_NAME@@': view_name,
        },
    )

    com.log_print('')
    dur = com.get_duration_ms(start_time)
    sd = com.get_duration_string(dur)
    s = f"Job {__name__} terminé en {sd}."
    com.log(s)
    com.log_print('')
    com.send_notif(s, __name__, dur)
