import qdd
import common as com

com.init_log('test_qdd')


def test_qdd():
    qdd.run_qdd(
        IN_DIR='test/',
        IN_FILE_1='qdd_test11',
        IN_FILE_2='qdd_test12',
        MAX_ROW_LIST=15,
        MAX_LINE_SPLIT=100,
        EQUAL_OUT=False,
        DIFF_OUT=False,
        OPEN_OUT_FILE=False,
    )


if __name__ == '__main__':
    test_qdd()
