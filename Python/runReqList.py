from ReqList import run_reqList

if __name__ == '__main__':
    run_reqList(
        MAX_BDD_CNX=4,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        NB_MAX_ELT_IN_STATEMENT=100,
        SL_STEP_QUERY=10,
    )
