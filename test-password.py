import unittest
from password import User
from password import Credentials

class TestPassword(unittest.TestCase):

    @classmethod
    def setUp(cls,self):
        self.newUser=User('james','kamau','jamie','james@kamau.com','0711223344')
        self.newCredential=Credentials('instagram','jamiek','james@k.com','igjameskamau')
        print('setup')

    @classmethod
    def tearDownClass(cls,self):
        print('teardown')

      
if __name__=='__main__':
    unittest.main()