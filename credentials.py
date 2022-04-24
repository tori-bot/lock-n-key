import pyperclip
class Credentials:
    #class that generates new instances of credentials
    credentials_list=[] #empty credentials list
    def __init__(self,account,username,email,password):
        self.account=account
        self.username=username
        self.email=email
        self.password=password

    def save_credential(self):
        #save credential objects to credentials list
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        #delete credential from list
        Credentials.credentials_list.remove(self)

    
    @classmethod
    def find_by_account(cls,account):
        #find credential by account from list
        for credential in cls.credentials_list:
            if credential.account==account:
                return credential

    @classmethod
    def credential_exists(cls,account):
        #find out if credential exists in list
        for credential in cls.credentials_list:
            if credential.account==account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        #returns all credentials in the list
        return cls.credentials_list

    @classmethod
    def copy_password(cls,account):
        #copy password to clipboard using pyperclip
        account_found=Credentials.find_by_account(account)
        pyperclip.copy(account_found.password)

