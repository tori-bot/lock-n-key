import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        #setup method to run before each test case
        self.new_credential=Credentials('twitter','tori-bot','tori.bot@gmail.com','qwerty')
        print('setup successful')

    def tearDown(self):
        #function to cleanup after each test is run
        Credentials.credentials_list=[]
        print('teardown successful')

        
        