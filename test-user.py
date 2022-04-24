import unittest
from user import User

class TestPassword(unittest.TestCase):
    def setUp(self):
        #method runs before each test case
        self.newUser=User('james','kamau','jamie','qwerty','james@kamau.com','0711223344')
        print('setup')

    def tearDown(self):
        User.users_list=[]
        print('teardown')

    

      
if __name__=='__main__':
    unittest.main()