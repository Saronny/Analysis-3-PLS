import sys
import csv
import json
import os

clear = lambda: os.system('cls') # a lambda for clearing the console





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

    
    def display(self):
        print(f"{self.name} lives at {self.street_address}.")
        print(f"email = {self.email}")


class Admin(Person):
    pass

        
def Login():
    # this is the login function it compares the input to the csv Member file 
    # When login == True it will make an instance of the Person class
    # username: reech1950
    # password: fgr5d4

    login_bool = False
    data = []
    print(""" ======PUBLIC LIBRARY=======""")
    username = input("Please enter username: ")
    password = input("Please Enter password: ")
    with open("Members.csv", mode = "r") as f:
            reader = csv.reader(f, delimiter = ";")
            for row in reader:
                if username == row[7] and password== row[8]:
                    login_bool = True
                    data += row
                
    if login_bool == True:
        user = Member(username, password, data)
        return user.display()
    else:
        clear()
        Login()
                
    



def main(): # Main function is for the start of the program
    done = False
    while done == False:
        print(""" ======PUBLIC LIBRARY=======\n[1].Login\n[2].Exit """)
        print(" ")
        choice = 0
        try:
           choice = int(input("Please enter choice: "))
        except:
            print("Numbers only.")

        if choice == 1:
            clear()
            Login()
            return
        elif choice == 2:
            sys.exit()
        else:
            print("Please enter correct number.")
main()


