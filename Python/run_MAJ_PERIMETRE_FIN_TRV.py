import SQL as sql
import common as com


def run_maj_perimetre(test=False):
    com.log("Lancement du job " + __name__)
    sql.download(
        ENV='DIRECT',
        BDD='CAPC5',
        QUERY_FILE='SQL/queries/e_CAPC5 (FIN_TRV_PERIMETRE).sql',
        OUT_FILE='C:/Py/IN/perimetre_fin_trv.csv',
        MAX_BDD_CNX=10,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=False,
        OPEN_OUT_FILE=False,
        SEND_NOTIF=False,
    )

    com.log(f"Job {__name__} terminé.")
    com.log_print('')
