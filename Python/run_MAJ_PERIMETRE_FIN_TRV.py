import sql
import common as com


def run_maj_perimetre(test=False):

    query_file = 'sql/queries/e_CAPC5 (FIN_TRV_PERIMETRE).sql'
    out_file = 'C:/Py/IN/perimetre_fin_trv.csv'
    if test:
        query_file = 'sql/queries/e_CAPC5 (FIN_TRV_PERIMETRE_TEST).sql'
        out_file = 'C:/Py/IN/perimetre_fin_trv_test.csv'

    com.log("Lancement du job " + __name__)
    sql.download(
        ENV='DIRECT',
        BDD='CAPC5',
        QUERY_FILE=query_file,
        OUT_FILE=out_file,
        MAX_BDD_CNX=10,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=False,
        OPEN_OUT_FILE=False,
        SEND_NOTIF=False,
    )

    com.log(f"Job {__name__} terminé.")
    com.log_print()
