import sql
import common as com

from datetime import datetime


def run_gen_out_file(test=False):
    date = datetime.now().strftime("%Y%m%d")
    query_file = 'sql/queries/e_CAPC5 (EDF_AFF_EC_QUOTIDIEN).sql'
    out_file = f'C:/Py/OUT/fin_trv_out_{date}.csv'
    if test:
        query_file = 'sql/queries/e_CAPC5 (EDF_AFF_EC_QUOTIDIEN_TEST).sql'
        out_file = 'C:/Py/OUT/perimetre_fin_trv_test.csv'

    com.log("Lancement du job " + __name__)
    sql.download(
        ENV='DIRECT',
        DB='CAPC5',
        QUERY_FILE=query_file,
        OUT_FILE=out_file,
        MAX_DB_CNX=10,
        MERGE_RG_FILES=True,
        EXPORT_RANGE=False,
        CHECK_DUP=False,
        OPEN_OUT_FILE=False,
        SEND_NOTIF=False,
    )

    com.log(f"Job {__name__} terminé.")
    com.log_print()
