from user import User
from credentials import Credentials
import random
import string

def register_user(fname,lname,username,password,email,phone_number):
    #function to register new user
    new_user=User(fname,lname,username,password,email,phone_number)
    return new_user

def user_exist_login(password):
    #find user by password so they can login
    return User.user_exist(password)

def create_account_credential(account,username,email,password):
    #function to create new credentials object
    new_credential=Credentials(account,username,email,password)
    return new_credential

def save_account_credential(credential):
    #save credential
    credential.save_credentials(credential)

