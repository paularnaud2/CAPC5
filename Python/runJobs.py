from run_AFF_FULL_FIN_TRV import run_aff
from run_SGE_FULL_FIN_TRV import run_sge
from run_MAJ_PERIMETRE_FIN_TRV import run_maj_perimetre

test = False
# test = True
if __name__ == '__main__':
    run_maj_perimetre()
    run_aff(test)
    run_sge(test)
