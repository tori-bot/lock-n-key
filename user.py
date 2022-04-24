class User:
    users_list=[]
    def __init__(self,fname,lname,username,password,email,phone_number):
        self.fname=fname
        self.lname=lname
        self.username=username
        self.password=password
        self.email=email
        self.phone_number=phone_number

    def save_user(self):
        #save user in user list
        User.users_list.append(self)
        

    
        

        