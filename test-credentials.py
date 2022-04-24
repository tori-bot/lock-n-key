import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        #setup method to run before each test case
        self.new_credential=Credentials('twitter','tori-bot','tori.bot@gmail.com','qwerty')
        

    def tearDown(self):
        #function to cleanup after each test is run
        Credentials.credentials_list=[]
        

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

    def test_find_by_account(self):
        #test of a credential can be found using account name
        self.new_credential.save_credential()
        test_credential=Credentials('instagram','joyous-cat','joy@cat.com','mnbvcxz')
        test_credential.save_credential()

        found_credential=Credentials.find_by_account('instagram')
        self.assertEqual(found_credential.email,test_credential.email)

    def test_credential_exists(self):
        #test if credential exists andretirn boolean
        self.new_credential.save_credential()
        test_credential=Credentials('instagram','joyous-cat','joy@cat.com','mnbvcxz')
        test_credential.save_credential()

        credential_exists=Credentials.credential_exists('instagram')

        self.assertTrue(credential_exists)

    def test_display_credentials(self):
        #test if list of all saved credentials is returned
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_password(self):
        #check that we are copying password from found credential to clipboard
        self.new_credential.save_credential()
        Credentials.copy_password('twitter')

        self.assertEqual(self.new_credential.password,pyperclip.paste())




if __name__=='__main__' :
    unittest.main()  