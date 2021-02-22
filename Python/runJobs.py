from common import init_log
init_log('runJobs')

if __name__ == '__main__':
    # from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre
    # run_maj_perimetre()

    from run_AFF_FULL_FIN_TRV import run_aff
    run_aff()

    from run_SGE_FULL_FIN_TRV import run_sge
    run_sge()

    # from run_GEN_OUT_FILE import run_gen_out_file
    # run_gen_out_file()

    # from common import mail
    # mail('fin_trv')
