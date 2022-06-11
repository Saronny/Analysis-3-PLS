import datetime
import sys
import csv
import json
import os
from datetime import date

clear = lambda: os.system('cls') # a lambda for clearing the console
user = object    #global testing object for user 

class Book:

    def __init__(self, author, country, imageLink, language, link, pages, title, isbn, year, bookItems):
        self.Author = author
        self.Country = country
        self.ImageLink = imageLink
        self.Language = language
        self.Link = link
        self.Pages = pages
        self.Title = title
        self.Isbn = isbn
        self.Year = year
        self.BookItems = bookItems


class BookItem(Book): #BookItem class inherits from Book class 

    def __init__(self, author, country, imageLink, language, link, pages, title, isbn, year, bookItems):
        super().__init__(author, country, imageLink, language, link, pages, title, isbn, year, bookItems)
        self.lent = False
    
class LoanItem(BookItem): #loan item class inherits from bookItem class 

    # date = datetime.datetime.now()
    # return_date = date + datetime.timedelta(days=30)

    def __init__(self, author, country, imageLink, language, link, pages, title, isbn, year, bookItems):
        super().__init__(author, country, imageLink, language, link, pages, title, isbn, year, bookItems)
        self.BorrowedBy = user.Username
        self.DateLent = datetime.datetime.now()
        self.ReturnTime = self.DateLent + datetime.timedelta(days=30)

    

class Catalog: 

    def __init__(self, list_of_books):
        self.List_of_books = list_of_books
        self.Length = len(self.List_of_books)

    def view(self):
        for book in self.List_of_books:
            print(book.Title)
            print("Availibility: " + str(book.BookItems))

    def Search(self, req):
        count = 0
        for book in self.List_of_books:
            if(req in book.Title or req.capitalize() in book.Title) :
                print(book.Author + " - " + book.Title)
                print("Availibility: " + str(book.BookItems))
                count += 1
            elif(req in book.Author or req.capitalize() in book.Author):
                print(book.Author + " - " + book.Title)
                print("Availibility: " + str(book.BookItems))
                count += 1
        if(count == 0): 
            print("no books found.")



class Library:

    def __init__(self, list_of_books, list_of_members):

        self.List_of_members = list_of_members
        self.Catalog_obj = Catalog(list_of_books)
    
    #def borrow_book(): this is in the class diagram
        #pass
    def list_books(self):
        return self.Catalog_obj.view()
        
    def return_book(self, bookItem):
        item = ""
        check = False
        if bookItem in user.Books:
            for books in user.Books:
                item = books
                check = True
                print("You have returned: " + item)
                break
        else:
            print("Invalid book")
                    
        if(check == True):
            new_data = []    
            with open ("Books.json", mode= "r") as f:
                temp = json.load(f)
                for book in temp:
                    if(book["title"] == item):
                        book["bookItems"] += 1
                    new_data.append(book)
                    
            with open ("Books.json", mode= "w") as f:
                json.dump(new_data, f)
        
            new_data = []
            with open ("Members.csv", mode= "r") as f:
                temp = csv.DictReader(f, delimiter= ";")
                for members in temp:
                    if(members["Username"]  == user.Username):
                        temp = members["Books"].split("-")
                        temp.remove(item)
                        if(len(temp) > 0): 
                            for item in temp:
                                members["Books"] += item + "-"
                        else:
                            members["Books"] = "None"
                    new_data.append(members)
                    
            with open ("Members.csv", mode= "w") as f:
                fieldnames = ["Number", "GivenName", "Surname", "StreetAddress", "ZipCode", "City", "EmailAddress", "Username", "Password", "TelephoneNumber", "Books"]
                write = csv.DictWriter(f, fieldnames=fieldnames)
                write.writeheader()
                write.writerows(new_data)
                load_library()
            	

    def lend_book(self, bookItem):
        items = self.Catalog_obj.List_of_books
        check = False
        if(len(user.Books) < 3):
            loanItem = object
            for book in items:
                if(bookItem == book.Title and book.BookItems > 0):
                    user.Books.append(LoanItem(book.Author, book.Country, book.ImageLink, book.Language, book.Link, book.Pages, book.Title, book.Isbn, book.Year, book.BookItems))
                    check = True
                    print("You have lend: " + book.Title)
                    break
        else:
            print("Book not availible")
        
        if(check == True):
            new_data = []    
            with open ("Books.json", mode= "r") as f:
                temp = json.load(f)
                for book in temp:
                    if(book["title"] == bookItem):
                        book["bookItems"] -= 1
                    new_data.append(book)
                    
            with open ("Books.json", mode= "w") as f:
                json.dump(new_data, f)
                
            new_data = []
            with open ("Members.csv", mode= "r") as f:
                temp = csv.DictReader(f, delimiter= ";")
                for members in temp:
                    if(members["Username"]  == user.Username):
                        if(members["Books"] == "None"):
                            members["Books"] = bookItem
                        else:
                            members["Books"] += "-" + bookItem; 
                    new_data.append(members)
                    
            with open ("Members.csv", mode= "w") as f:
                fieldnames = ["Number", "GivenName", "Surname", "StreetAddress", "ZipCode", "City", "EmailAddress", "Username", "Password", "TelephoneNumber", "Books"]
                write = csv.DictWriter(f, fieldnames=fieldnames)
                write.writeheader()
                write.writerows(new_data)
                load_library()
                
                
                

    def add_book(self, ):
        pass

    def edit_book():
        pass

    def delete_book():
        pass
    
    def list_members(self):
        for member in self.List_of_members:
            print(member) 

    def add_members():
        pass

    def delete_members():
        pass

class Person:

    #;GivenName;Surname;StreetAddress;ZipCode;City;EmailAddress;Username;Password;TelephoneNumber

    def __init__(self, id, name, surname, address, zipCode, city, email, username, password, telephoneNumber, books):

        self.Id = id
        self.Name= name
        self.Surname = surname
        self.Adress = address
        self.ZipCode = zipCode
        self.City = city
        self.Email = email
        self.Username = username
        self.Password = password
        self.TelephoneNumber = telephoneNumber
        self.Books = books


    def display(self):
        print(f"Account of {self.Username}")
 


class Member(Person):
    def __intit__(self):
        super().__init__(self)
        
    def display_books(self):
        for books in self.Books:
            print(books.Title + "\n") 
    
    
    def display_Message(self):
        print(f"Welcome {self.Username}")
        

class LibaryAdmin(Person):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_Message(self):
        print(f"Welcome {self.username}")

    def display_Members(self):
        x = library_obj.list_members()
        for member in x:
            print(member + "\n")



def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)



def load_library(): # Function for object library
    list_of_books = []
    member_list = []
    bookitemlist = []
    try:
        with open("Books.json") as f:
            book_data = json.load(f)
            check = False
            for book in book_data:
                if("bookItems" in book):
                    list_of_books.append(Book(book["author"], book["country"], book["imageLink"], book["language"], book["link"], book["pages"], book["title"], book["ISBN"], book["year"], book["bookItems"]))
                    check = True
                else:
                    book["bookItems"] = 3
                    check = False
                    list_of_books.append(Book(book["author"], book["country"], book["imageLink"], book["language"], book["link"], book["pages"], book["title"], book["ISBN"], book["year"], book["bookItems"]))
                        
        if(check == False):
            write_json(book_data, "Books.json")        
    
    except:
        print("Error: Books.json not found.")

    
    try:
        check = False
        csv_list = []
        with open("Members.csv", mode = "r") as f:
            reader = csv.DictReader(f, delimiter = ";")
            for dict in reader:
                if("Books" in dict):
                    check = True
                    member_list.append(Member(dict["Number"], dict["GivenName"], dict["Surname"], dict["StreetAddress"], dict["ZipCode"], dict["City"], dict["EmailAddress"], dict["Username"], dict["Password"], dict["TelephoneNumber"], dict["Books"]))
                else:
                    csv_list.append(dict)
                    check = False        

        if(check == False):
            with open("Members.csv", mode = "w") as f:
                header = ["Number", "GivenName", "Surname", "StreetAddress", "ZipCode", "City", "EmailAddress", "Username", "Password", "TelephoneNumber", "Books"]
                write = csv.DictWriter(f, fieldnames= header, delimiter= ";")
                write.writeheader()
                for dict in csv_list:
                    dict["Books"] = "None"
                    write.writerow(dict)
                    member_list.append(Member(dict["Number"], dict["GivenName"], dict["Surname"], dict["StreetAddress"], dict["ZipCode"], dict["City"], dict["EmailAddress"], dict["Username"], dict["Password"], dict["TelephoneNumber"], dict["Books"]))
                        
    except:
        print("Error: Members.csv not found.")
    

    return Library(list_of_books, member_list)


library_obj = load_library() #Library object


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
        user = LibaryAdmin(username, password)
        clear()
        return main(5)

    for member in library_obj.List_of_members:
        if(username == member.Username and password == member.Password):
            user = member
            login_bool = True
                
    if login_bool == True:
        clear()
        return main(1)
    else:
        clear()
        print("username or password incorrect")
        Login()








def main(screen = 0): # Main function is for the start of the program
    global library_obj

    def Back(n):      #simple back function
        print("")
        b = input("Enter 1 to go back: ")    
        if(b == "1"):    
            clear()
            return main(n)
        else:
            Back(n)

    if screen == 0: #login screen
        choice = 0
        print(""" ======PUBLIC LIBRARY=======""")
        print("[1] Login")
        print("[2] Exit")
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

    if screen == 1: #Member main screen
        choice = 0
        print(""" ======PUBLIC LIBRARY=======""")
        user.display_Message()
        print("[1] Check catalog")
        print("[2] Search book")
        print("[3] Return book")
        print("[4] Lend book")
        print("[5] Log out")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(1)

        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            library_obj.list_books()
            Back(1)

        elif choice == 2: ## search book option screen ##
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            req = input("Please enter a Title or author: ")
            if(req != ""):
                library_obj.Catalog_obj.Search(req)
                Back(1)
          

        elif choice == 3:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            user.display_books()
            req = input("Please enter Title: ")
            if(req != ""):
                library_obj.return_book(req)
                Back(1)
            
        elif choice == 4:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            book = input("Please enter a Title: ")
            if(book != ""):
                library_obj.lend_book(book)
                Back(1)
        
        elif choice == 5:
            clear()
            return main()

        else:
            print("please enter correct number")
            main(1)



    if screen == 5: #Admin main screen
        print(""" ======PUBLIC LIBRARY=======""") 
        user.display_Message()
        print("[1] Book options")
        print("[2] Member options")
        print("[3] System options")
        print("[4] Log out")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(5)

        if choice == 1: 
            clear()
            main(6)
        elif choice == 2: 
            clear()
            main(7)
        elif choice == 3:
            clear()
            main(8)
        elif choice == 4:
            clear()
            main()
        else:
            clear()
            print("Please enter correct number")
            main(5)
    

    if screen == 6: #Admin book menu screen
        print(""" ======PUBLIC LIBRARY=======""") 
        print("[1] View catalog")
        print("[2] Search book")
        print("[3] Add book(s)")
        print("[4] Edit book")
        print("[5] delete book")
        print("[6] Back")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(6)
        
        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            library_obj.list_books()
            Back(6)

        elif choice == 2:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            req = input("Please enter a Title or author: ")
            if(req != ""):
                library_obj.Catalog_obj.Search(req)
                Back(6)
        
        elif choice == 3:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(6)
        
        elif choice == 4:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(6)

        elif choice == 5:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(6)
        
        elif choice == 6:
            clear()
            main(5)
        
        else:
            clear()
            print("Please enter correct number")
            main(6)
            

    if screen == 7: #Admin member menu screen
        print(""" ======PUBLIC LIBRARY=======""") 
        print("[1] View Members")
        print("[2] Add Member(s)")
        print("[3] Edit Member")
        print("[4] Delete Member")
        print("[5] Back")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(7)
        
        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            library_obj.list_members()
            Back(7)

        elif choice == 2:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(7)
        
        elif choice == 3:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(7)
        
        elif choice == 4:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(7)

        elif choice == 5:
            clear()
            main(5)
        
        else:
            clear()
            print("Please enter correct number")
            main(7)

    if screen == 8: #Admin system menu screen 
        print(""" ======PUBLIC LIBRARY=======""")
        print("[1] Make back-up")
        print("[2] Restore back-up")
        print("[3] Back")
        try:
            choice = int(input("Please enter choice: "))
        except:
            clear()
            print("Numbers only")
            main(8)
        
        if choice == 1:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(8)
        
        elif choice == 2:
            clear()
            print(""" ======PUBLIC LIBRARY=======""")
            print("Wip")
            Back(8)
        
        elif choice == 3:
            clear()
            main(5)

        else:
            clear()
            print("Please enter correct number")
            main(8)

main()


