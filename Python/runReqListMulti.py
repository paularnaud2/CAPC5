from ReqList import run_reqList
from ReqList import gl

if __name__ == '__main__':
    # QDD SMO ADAM/GINKO
    ""
    BDD = 'ADAM'
    QUERY_FILE = 'ReqList/queries/ADAM_INFOS_SRV.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.OUT_FILE)

    BDD = 'GINKO'
    QUERY_FILE = 'ReqList/queries/GINKO_INFOS_SMO.sql'
    run_reqList(BDD, QUERY_FILE, gl.OUT_FILE, gl.OUT_FILE)
    ""

    # QDD ctr_frn SGE/GINKO
    """
    BDD = 'SGE'
    QUERY_FILE = 'ReqList/queries/PRM_INFOS_PDL.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.OUT_FILE)

    BDD = 'GINKO'
    QUERY_FILE = 'ReqList/queries/GINKO_INFOS_PDS.sql'
    run_reqList(BDD, QUERY_FILE, gl.OUT_FILE, gl.OUT_FILE)
    """

    # QDD oppositions ADAM/GINKO
    """
    BDD = 'SGE'
    QUERY_FILE = 'ReqList/queries/PRM_ETAT-SI-NIV.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.IN_FILE)

    BDD = 'ADAM'
    QUERY_FILE = 'ReqList/queries/ADAM_OPPENR.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.IN_FILE)
    """

    # QDD ctr SGE/GINKO
    """
    BDD = 'SGE'
    QUERY_FILE = 'ReqList/queries/SGE_ETAT_SI.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.IN_FILE)

    BDD = 'GINKO'
    QUERY_FILE = 'ReqList/queries/GINKO_DATE_MODIF.sql'
    run_reqList(BDD, QUERY_FILE, gl.IN_FILE, gl.IN_FILE)
    """
