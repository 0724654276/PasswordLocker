import unittest 
from user import User 

class TestUser(unittest.TestCase):

    def setUp(self):
        
        self.user_list = User("macharia","kamakia","0724654276","machariakamakia@gmail.com","password")

    def test_init(self):
        
        self.assertEqual(self.user_list.first_name,"macharia")
        self.assertEqual(self.user_list.last_name,"kamakia")
        self.assertEqual(self.user_list.phone_number,"0724654276")
        self.assertEqual(self.user_list.email,"georgekamakia@gmail.com")
        self.assertEqual(self.user_list.password,"password")
if __name__ == '__main__':
    unittest.main()   