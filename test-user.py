import unittest
from user import User

class TestPassword(unittest.TestCase):
    def setUp(self):
        #method runs before each test case
        self.new_user=User('james','kamau','jamie','qwerty','james@kamau.com','0711223344')

    def tearDown(self):
        #method to clean up after each test is run
        User.users_list=[]

    def test_init(self):
        #test if object is initiated properly
        self.assertEqual(self.new_user.fname,'james')
        self.assertEqual(self.new_user.lname,'kamau')
        self.assertEqual(self.new_user.username,'jamie')
        self.assertEqual(self.new_user.password,'qwerty')
        self.assertEqual(self.new_user.email,'james@kamau.com')
        self.assertEqual(self.new_user.phone_number,'0711223344')

      
if __name__=='__main__':
    unittest.main()