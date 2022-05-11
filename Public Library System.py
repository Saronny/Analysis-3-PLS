import sys
import csv
import json
import os

clear = lambda: os.system('cls') # a lambda for clearing the console
user = object    #global testing object for user 

class Library:

    def __init__(self, list_of_book_items, list_of_members, catalog):

        self.list_of_book_items =  list_of_book_items
        self.list_of_members = list_of_members
        self.catalog = catalog
    
    #def borrow_book(): this is in the class diagram
        #pass
    def list_books(self):
        return self.catalog
        
    def return_book():
        pass

    def lend_book():
        pass

    def add_book():
        pass

    def edit_book():
        pass

    def delete_book():
        pass
    
    def list_members(self):
        return self.list_of_members

    def add_members():
        pass

    def delete_members():
        pass

def load_library(): # Function for object library
    cat = []
    memberList = []
    bookitemlist = []
    with open("Books.json") as f:
        book_data = json.load(f)
        for i in book_data:
            cat.append(i["title"])

    with open("Members.csv", mode = "r") as f:
                reader = csv.reader(f, delimiter = ";")
                for row in reader:
                    memberList.append(row[7])
    return Library([], memberList, cat)


library_obj = load_library() #Library object



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
    
    def display_books(self):
        x = library_obj.list_books()
        for books in x: 
            print(books + "\n")
        


class Admin(Person):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_Message(self):
        print(f"Welcome {self.username}")

    def display_Members(self):
        x = library_obj.list_members()
        for member in x:
            print(member + "\n")



    



def Login():
    # this is the login function it compares the input to the csv Member file 
    # When login_bool == True it will make an instance(user) of the Member class/ Admin class
    # username: reech1950
    # password: fgr5d4
    global user 
    login_bool = False
    data = []
    print(""" ======PUBLIC LIBRARY=======""")
    username = input("Please enter username: ")
    password = input("Please Enter password: ")

    if username == "admin" and password == "admin123": #hardcoded admin login
        user = Admin(username, password)
        clear()
        return main(5)
    else:
        with open("Members.csv", mode = "r") as f:
                reader = csv.reader(f, delimiter = ";")
                for row in reader:
                    if username == row[7] and password== row[8]:
                        login_bool = True
                        data += row
                
    if login_bool == True:
        user = Member(username, password, data)
        clear()
        return main(1)
    else:
        clear()
        print("username or password incorrect")
        Login()








def main(screen = 0): # Main function is for the start of the program

    def Back(n):      #simple back function
        print("")
        b = input("Press 1 to go back")    
        if(b == "1"):    
            clear()
            return main(n)
        else:
            Back(n)


    if screen == 0: #login screen
        login = False
        while login == False:
            choice = 0
            print(""" ======PUBLIC LIBRARY=======""")
            print("[1] Login")
            print("[2] Exit")
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
        choice = 0
        print(""" ======PUBLIC LIBRARY=======""")
        user.display_Message()
        print("[1] Check catalog")
        print("[2] Search book")
        print("[3] Return book")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(1)

        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            user.display_books()
            Back(1)

        elif choice == 2:
            clear()
            print("WIP")

        elif choice == 3:
            clear()
            print("WIP")

    if screen == 5: #Admin screen
        print(""" ======PUBLIC LIBRARY=======""") 
        user.display_Message()
        print("[1] View Members")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(5)

        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            user.display_Members()
            Back(5)
        else:
            print("WIP")
main()


