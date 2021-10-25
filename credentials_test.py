import unittest #testing module
import pyperclip
from credentials import Credential
class TestCredentials(unittest.TestCase):
    """
    Test class for credentials
    Args:
    unittest.TestCase: Testcase class that helps in creating tests
    """
    def setUp(self):
        self.new_credentials = Credential("georgekamakia@gmail.com", "clearscore", 12345678)

    def test_init(self):
        self.assertEqual(self.new_credentials.email, "georgekamakia@gmail.com")
        self.assertEqual(self.new_credentials.platform, "clearscore")
        self.assertEqual(self.new_credentials.password, 12345678)

if __name__ == "__main__":
    unittest.main()