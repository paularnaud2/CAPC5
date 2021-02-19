import common as com


def test_common():
    com.init_log('test_common', True)
    com.mail(
        mail_name='fin_trv',
        recipients_file='recipients_test.txt',
        subject_file='subject_test.txt',
    )


if __name__ == '__main__':
    test_common()
