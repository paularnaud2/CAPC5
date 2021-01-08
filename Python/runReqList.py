from common import init_log
init_log('runReqList', 'C:/Py/')

if __name__ == '__main__':
    from ReqList import run_reqList
    run_reqList(
        MAX_BDD_CNX=8,
        SQUEEZE_JOIN=True,
        SQUEEZE_SQL=False,
        CHECK_DUP=True,
        NB_MAX_ELT_IN_STATEMENT=500,
        SL_STEP_QUERY=50,
    )
