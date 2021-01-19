from common import init_log
init_log('test_runJobs')


def test_runJobs():

    from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre
    run_maj_perimetre(test=True)

    from run_AFF_FULL_FIN_TRV import run_aff
    run_aff(test=True)

    from run_SGE_FULL_FIN_TRV import run_sge
    run_sge(test=True)

    from common import mail
    mail(
        mail_name='fin_trv',
        recipients_file='recipients_test.txt',
        subject_file='subject_test.txt',
    )


if __name__ == '__main__':
    test_runJobs()
