from Tests.TestCase import hudlTestCase
import unittest


def cases():
    cases = unittest.TestSuite()
    cases.addTest(hudlTestCase('test_login_page'))
    cases.addTest(hudlTestCase('test_sign_in'))
    cases.addTest(hudlTestCase('test_invalid_sign_in'))
    cases.addTest(hudlTestCase('test_reset_password'))
    cases.addTest(hudlTestCase('test_reset_password_with_invalid_email'))
    return cases


if __name__ == "__main__":
    test_runner = unittest.TextTestRunner()
    test_runner.run(cases())

