from services.Login import Login
from services.servicehelpers.IsInfoValid import IsInfoValid
from ui.MainMenu import MainMenu
import getpass
import os
import time

class LoginMenu:
    def __init__(self): 
        self.__login = Login()
        self.__getlogininfo = IsInfoValid()
    def login_menu(self):
        os.system('cls') #  hreinsar console gluggann
        while True:
            print("Please enter your credentials.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            valid_user = self.__login.validUser(username, password)
            if valid_user:
                self.isadmin = self.__login.isAdmin(username) #athugar hvort notandi sé með adminréttindi
                self.fullname = self.__getlogininfo.get_fullname
                #MainMenu.main_menu(self, check_if_admin, username, fullname)
                MainMenu.main_menu(self)
            else: # ef annaðhvort username eða password er vitlaust
                os.system('cls')
                print("Wrong Username and/or Password\n")
    def header(self, check_if_admin, username):
        if check_if_admin:
            admintag = "(A)"
        else:
            admintag = ""
        print("------------------------------------")
        print("Welcome {}{} {}".format(username, admintag, time.ctime()))
        return