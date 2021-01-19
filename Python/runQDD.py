import qdd
from common import init_log
init_log('run_qdd')

if __name__ == '__main__':
    qdd.run_qdd(
        IN_DIR='test/',
        IN_FILE_1='qdd_test11',
        IN_FILE_2='qdd_test12',
        MAX_ROW_LIST=15,
        MAX_LINE_SPLIT=100,
    )
