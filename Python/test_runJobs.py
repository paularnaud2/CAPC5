from common import mail
from common import init_log
from run_AFF_FULL_FIN_TRV import run_aff
from run_SGE_FULL_FIN_TRV import run_sge
from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre

init_log('test_runJobs')


def test_runJobs():
    run_maj_perimetre(test=True)
    run_aff(test=True)
    run_sge(test=True)
    mail(
        mail_name='fin_trv',
        recipients_file='recipients_test.txt',
        subject_file='subject_test.txt',
    )


if __name__ == '__main__':
    test_runJobs()
