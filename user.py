from pickle import TRUE


class User:
    users_list=[]
    def __init__(self,fname,lname,username,password,email,phone_number):
        self.fname=fname
        self.lname=lname
        self.username=username
        self.password=password
        self.email=email
        self.phone_number=phone_number

    def register_user(self):
        #save user in user list
        User.users_list.append(self)
        

    @classmethod
    def user_exist(cls,username,password):
        #check if user is registered so they can login
        for user in cls.users_list:
            if user.username==username and user.password==password:
                return True
        return False

    




    
        

        