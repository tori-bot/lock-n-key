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