import time
import sql
import common as com

from datetime import datetime
from reqlist import run_reqList


def run_aff(test=False):
    # Définition des variables
    start_time = time.time()
    date = datetime.now().strftime("%Y%m%d")
    in_file = 'C:/Py/IN/perimetre_fin_trv.csv'
    out_file = f'C:/Py/OUT/out_AFF_FULL_FIN_TRV_{date}.csv'
    table_name = f'AFF_FULL_{date}'
    view_name = 'AFF'
    max_elt_insert = 10000
    max_elt_st = 500
    max_bdd_cnx = 8
    sl_step_query = 100

    if test:
        in_file = 'C:/Py/IN/perimetre_fin_trv_test.csv'
        out_file = f'C:/Py/OUT/out_test_AFF_{date}.csv'
        table_name = f'AFF_TEST_{date}'
        view_name = 'AFF_TEST'
        max_elt_insert = 40
        max_elt_st = 10
        max_bdd_cnx = 6
        sl_step_query = 10

    squeeze_downl = False
    (squeeze_downl, squeeze_create_table) = sql.check_restart(squeeze_downl)

    com.log("Lancement du job " + __name__)
    if not squeeze_downl:
        com.log('Export SGE\
------------------------------------------------------------')
        run_reqList(
            ENV='PROD',
            BDD='SGE',
            QUERY_FILE='reqlist/queries/SGE_SUIVI_FIN_TRV_AFF.sql',
            IN_FILE=in_file,
            OUT_FILE=out_file,
            MAX_BDD_CNX=max_bdd_cnx,
            SL_STEP_QUERY=sl_step_query,
            NB_MAX_ELT_IN_STATEMENT=max_elt_st,
            OPEN_OUT_FILE=False,
            SQUEEZE_JOIN=True,
            SQUEEZE_SQL=False,
            CHECK_DUP=False,
            SEND_NOTIF=False,
        )

    if not squeeze_create_table:
        com.log(f'Création de la table {table_name}\
------------------------------------')
        sql.execute(
            ENV='DIRECT',
            BDD='CAPC5',
            SCRIPT_FILE='sql/procs/create_table_aff.sql',
            VAR_DICT={'TABLE_NAME': table_name},
            PROC=True,
        )

    com.log('Export des données importées dans la table créée\
----------------------')
    sql.upload(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='sql/scripts/insert_table_aff.sql',
        VAR_DICT={'TABLE_NAME': table_name},
        UPLOAD_IN=out_file,
        NB_MAX_ELT_INSERT=max_elt_insert,
    )

    com.log(f'Mise à jour de la vue {view_name}\
-----------------------------------')
    sql.execute(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='sql/scripts/update_view_aff.sql',
        VAR_DICT={
            'TABLE_NAME': table_name,
            'VIEW_NAME': view_name,
        },
    )

    dur = com.get_duration_ms(start_time)
    sd = com.get_duration_string(dur)
    s = f"Job {__name__} terminé en {sd}."
    com.log(s)
    com.log_print()
    com.send_notif(s, __name__, dur)
