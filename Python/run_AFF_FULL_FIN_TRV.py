import time
import SQL as sql
import common as com

from datetime import datetime
from ReqList import run_reqList


def run_aff(test=False):
    # Définition des variables
    start_time = time.time()
    date = datetime.now().strftime("%Y%m%d")
    in_file = 'C:/Py/IN/perimetre_aff_full.csv'
    out_file = f'C:/Py/OUT/out_AFF_FULL_FIN_TRV_{date}.csv'
    table_name = f'AFF_FULL_{date}'
    view_name = 'AFF'
    max_elt_insert = 20000
    max_elt_st = 1000
    max_bdd_cnx = 8

    if test:
        in_file = 'C:/Py/IN/in_test.csv'
        out_file = f'C:/Py/OUT/out_test_{date}.csv'
        table_name = f'AFF_TEST_{date}'
        view_name = 'AFF_TEST'
        max_elt_insert = 40
        max_elt_st = 100
        max_bdd_cnx = 2

    squeeze_export = False
    (squeeze_export, squeeze_create_table) = sql.check_restart(squeeze_export)

    if not squeeze_export:
        com.log('Export SGE\
------------------------------------------------------------')
        run_reqList(
            ENV='PROD',
            BDD='SGE',
            QUERY_FILE='ReqList/queries/SGE_SUIVI_FIN_TRV_AFF.sql',
            IN_FILE=in_file,
            OUT_FILE=out_file,
            MAX_BDD_CNX=max_bdd_cnx,
            SL_STEP_QUERY=50,
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
            SCRIPT_FILE='SQL/procs/create_table_aff.sql',
            VAR_DICT={'@@TABLE_NAME@@': table_name},
            PROC=True,
        )

    com.print_com('')
    com.log('Export des données importées dans la table créée\
----------------------')
    sql.upload(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='SQL/scripts/insert_table_aff.sql',
        VAR_DICT={'@@TABLE_NAME@@': table_name},
        IN_DIR=out_file,
        NB_MAX_ELT_INSERT=max_elt_insert,
    )

    com.print_com('')
    com.log(f'Mise à jour de la vue {view_name}\
-----------------------------------')
    sql.execute(
        ENV='DIRECT',
        BDD='CAPC5',
        SCRIPT_FILE='SQL/scripts/update_view_aff.sql',
        VAR_DICT={
            '@@TABLE_NAME@@': table_name,
            '@@VIEW_NAME@@': view_name,
        },
    )

    com.print_com('')
    dur = com.get_duration_ms(start_time)
    s = "Traitement terminé en {}."
    s = s.format(com.get_duration_string(dur))
    com.log(s)
    com.send_notif(s, __name__, dur)
