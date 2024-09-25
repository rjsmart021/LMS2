import configparser
import pandas as pd
from sql_queries import*
import mysql.connector
DB_NAME_DEFAULT = "SQL_1"
DB_USER = "root"
DB_PASSWORD = "HHappiness0621#"

REATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id),
);
Authors Table:
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);
Users Table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);
Borrowed Books Table:
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

#Connect to default database
def connect_database():
    """ COnnect to the MySQL database and return the connection object """

    #Database connection parameters 
    db_name = "e_commerce_db"
    user = "user"
    password = "password"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection si sucessful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None
Create a database in your MySQL Workbench and fill the db_name, user and password with yours, then use that function to create a connection like:
conn = connect_database()
And use it inside the functions to perform the different operations, for example, this is a function to inser a member:
def add_member(id, name, age):
    """
    Adds a new member to the 'Members' table.
    This will also handle duplicate ID and constraint violations.
    """
    conn = connect_database()
    if conn is not None: 
        try:
            cursor = conn.cursor()
            sql_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (id, name, age))
            conn.commit()
            print(f"Member {name} added successfully.")
        except Exception as e:
            print(f"Error while adding member: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")
cur = conn.cursor
#Add SQL Database
cur.execute("""CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);""")
conn.commit()
cur.execute("""CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);""")
conn.commit()
#Close connction
conn.close()
import re

class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
        print(f"Publication Date: {self.publication_date}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print("Sorry, the book is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.availability = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print("You have not borrowed this book.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.library_id}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Biography: {self.biography}")

def add_new_book(books):
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    book = Book(title, author, isbn, genre, publication_date)
    books.append(book)
    print("Book added successfully.")

def borrow_book(user, books):
    title = input("Enter title of the book to borrow: ")
    for book in books:
        if book.title.lower() == title.lower():
            user.borrow_book(book)
            return
    print("Book not found.")

def return_book(user, books):
    title = input("Enter title of the book to return: ")
    for book in books:
        if book.title.lower() == title.lower():
            user.return_book(book)
            return
    print("Book not found.")

def search_book(books):
    title = input("Enter title of the book to search: ")
    for book in books:
        if book.title.lower() == title.lower():
            book.display_info()
            return
    print("Book not found.")

def display_all_books(books):
    print("All Books:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.title}")

def add_new_user(users):
    name = input("Enter name of the user: ")
    library_id = input("Enter library ID of the user: ")
    user = User(name, library_id)
    users.append(user)
    print("User added successfully.")

def view_user_details(users):
    library_id = input("Enter library ID of the user: ")
    for user in users:
        if user.library_id.lower() == library_id.lower():
            user.display_info()
            return
    print("User not found.")

def display_all_users(users):
    print("All Users:")
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.name} (Library ID: {user.library_id})")

def add_new_author(authors):
    name = input("Enter name of the author: ")
    biography = input("Enter biography of the author: ")
    author = Author(name, biography)
    authors.append(author)
    print("Author added successfully.")

def view_author_details(authors):
    name = input("Enter name of the author: ")
    for author in authors:
        if author.name.lower() == name.lower():
            author.display_info()
            return
    print("Author not found.")

def display_all_authors(authors):
    print("All Authors:")
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.name}")

def main():
    books = []
    users = []
    authors = []

    # Add a default user
    add_new_user(users)

    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            book_operations_menu(books, users)
        elif choice == '2':
            user_operations_menu(users)
        elif choice == '3':
            author_operations_menu(authors)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def book_operations_menu(books, users):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_book(books)
        elif choice == '2':
            borrow_book(users[0], books)  # assuming there's only one user for simplicity
        elif choice == '3':
            return_book(users[0], books)  # assuming there's only one user for simplicity
        elif choice == '4':
            search_book(books)
        elif choice == '5':
            display_all_books(books)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def user_operations_menu(users):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_user(users)
        elif choice == '2':
            view_user_details(users)
        elif choice == '3':
            display_all_users(users)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def author_operations_menu(authors):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_author(authors)
        elif choice == '2':
            view_author_details(authors)
        elif choice == '3':
            display_all_authors(authors)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
