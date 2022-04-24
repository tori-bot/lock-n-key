from curses.ascii import US
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

    def test_register_user(self):
        #test if user is saved in list
        self.new_user.register_user()
        self.assertEqual(len(User.users_list),1)

    def test_user_exist(self):
        #check if user exists in users list
        self.new_user.register_user()
        test_user=User('joy','cat','kitcat','mnbvcxz','joy@cat.com','0712345678')
        test_user.register_user()

        user_exists=User.user_exist('mnbvcxz')
        self.assertTrue(user_exists)




      
if __name__=='__main__':
    unittest.main()