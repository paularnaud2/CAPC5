from common import init_log
init_log('runJobs', 'C:/Py/')

if __name__ == '__main__':
    from run_AFF_FULL_FIN_TRV import run_aff
    from run_SGE_FULL_FIN_TRV import run_sge
    # from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre

    # run_maj_perimetre()
    run_aff(test=True)
    run_sge(test=True)
