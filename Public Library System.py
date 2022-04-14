import sys
import csv
import json
import os

clear = lambda: os.system('cls') # a lambda for clearing the console
user = object    #global testing object for user 



class Person:

    def __init__(self, username, password, data):

        
        self.username = username
        self.password = password
        self.ID = data[0]
        self.name = data[1]
        self.surname = data[2]
        self.street_address = data[3]
        self.zip_code = data[4]
        self.city = data[5]
        self.email = data[6]

    def display(self):
        print(f"Account of {self.username}")



class Member(Person):
    def __intit__(self, data):
        super().__init__(self, username, password, data)
        #self.borrowedbook = ?

    
    def display_Message(self):
        print(f"Welcome {self.username}")
    
        


class Admin(Person):
    def __init__(self, username, password):

        self.username = username
        self.password = password

    def display(self):
        print(f"Welcome {self.username}")
    



def Login():
    # this is the login function it compares the input to the csv Member file 
    # When login_bool == True it will make an instance(user) of the Member class/ Admin class
    # username: reech1950
    # password: fgr5d4

    login_bool = False
    data = []
    print(""" ======PUBLIC LIBRARY=======""")
    username = input("Please enter username: ")
    password = input("Please Enter password: ")

    if username == "admin" and password == "admin123": #hardcoded admin login
        login_bool == True
    else:
        with open("Members.csv", mode = "r") as f:
                reader = csv.reader(f, delimiter = ";")
                for row in reader:
                    if username == row[7] and password== row[8]:
                        login_bool = True
                        data += row
                
    if login_bool == True:
        global user
        if username == "admin" and password == "admin123":
            user = Admin(username, password)
            return main(2)
        else :
            user = Member(username, password, data)
            clear()
            return main(1)
    else:
        clear()
        print("username or password incorrect")
        Login()


                
   



def main(screen = 0): # Main function is for the start of the program
    if screen == 0: #login screen
        login = False
        while login == False:
            choice = 0
            print(""" ======PUBLIC LIBRARY=======\n[1].Login\n[2].Exit """)
            print(" ")
            try:
                choice = int(input("Please enter choice: "))
            except:
                clear()
                print("Numbers only.")

            if choice == 1:
                clear()
                return Login()
            elif choice == 2:
                sys.exit()
            else:
                print("Please enter correct number.")

    if screen == 1: #Member screen
        print(""" ======PUBLIC LIBRARY=======""")
        user.display_Message()

    if screen == 2: #Admin screen
        print(""" ======PUBLIC LIBRARY=======""")
        user.display_Message()
main()


