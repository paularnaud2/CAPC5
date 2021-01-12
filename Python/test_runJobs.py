import os
from common import init_log
from common import g
init_log('test_runJobs', 'C:/Py/')


def test_runJobs():
    test = True

    from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre
    run_maj_perimetre(test)

    from run_AFF_FULL_FIN_TRV import run_aff
    run_aff(test)

    g.MIN_DUR_NOTIF_TRIGGER = 1
    from run_SGE_FULL_FIN_TRV import run_sge
    run_sge(test)

    from common import mail
    mail(
        mail_name='fin_trv',
        recipients_file='recipients_test.txt',
        subject_file='subject_test.txt',
    )

    os.startfile(g.paths['LOG'] + g.LOG_FILE)


if __name__ == '__main__':
    test_runJobs()
