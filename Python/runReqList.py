from ReqList import run_reqList

if __name__ == '__main__':
    run_reqList(
        MAX_BDD_CNX=8,
        SQUEEZE_JOIN=False,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        SL_STEP_QUERY=10,
    )
