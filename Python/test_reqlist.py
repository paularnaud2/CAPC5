import common as com

from test import gl
from common import g
from reqlist import run_reqList
from reqlist import join_main


def join():

    run_reqList(
        QUERY_FILE='reqlist/queries/e_RL.sql',
        IN_FILE=f"{g.paths['IN']}in.csv",
        OUT_FILE=f"{g.paths['OUT']}export_RL_{BDD}_{date}.csv",
        MAX_BDD_CNX=8,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=True,
        CHECK_DUP=True,
        NB_MAX_ELT_IN_STATEMENT=500,
        SL_STEP_QUERY=50,
    )
