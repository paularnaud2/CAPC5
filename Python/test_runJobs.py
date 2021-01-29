import common as com

from run_AFF_FULL_FIN_TRV import run_aff
from run_SGE_FULL_FIN_TRV import run_sge
from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre
from run_GEN_OUT_FILE import run_gen_out_file


def test_runJobs():
    com.init_log('test_runJobs', True)
    run_maj_perimetre(test=True)
    run_aff(test=True)
    run_sge(test=True)
    run_gen_out_file(test=True)
    # com.mail(
    #     mail_name='fin_trv',
    #     recipients_file='recipients_test.txt',
    #     subject_file='subject_test.txt',
    # )


if __name__ == '__main__':
    test_runJobs()
