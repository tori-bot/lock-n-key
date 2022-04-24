from user import User
from credentials import Credentials
import random
import string

def register(fname,lname,username,password,email,phone_number):
    #function to register new user
    new_user=User(fname,lname,username,password,email,phone_number)
    return new_user