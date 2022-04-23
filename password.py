class User:
    def __init__(self,fname,lname,username,email,phone_number):
        self.fname=fname
        self.lname=lname
        self.username=username
        self.email=email
        self.phone_number=phone_number
        
class Credentials:
    def __init__(self,account,username,email,password):
        self.account=account
        self.username=username
        self.email=email
        self.password=password
        