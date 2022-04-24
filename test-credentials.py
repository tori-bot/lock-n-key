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

    def test_init(self):
        #test if object is initialized properly
        self.assertEqual(self.new_credential.account,'twitter')
        self.assertEqual(self.new_credential.username,'tori-bot')
        self.assertEqual(self.new_credential.email,'tori.bot@gmail.com')
        self.assertEqual(self.new_credential.password,'qwerty')

    def test_save_credential(self):
        #test if credential is saved in list
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        #check if more than one credential can be saved in the list
        self.new_credential.save_credential()
        test_credential=Credentials('instagram','joyous-cat','joy@cat.com','mnbvcxz')
        test_credential.save_credential()
        
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        #test if credential can be removed rom list
        self.new_credential.save_credential()
        test_credential=Credentials('instagram','joyous-cat','joy@cat.com','mnbvcxz')
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

        




if __name__=='__main__' :
    unittest.main()  