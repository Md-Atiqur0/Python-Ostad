import add_books
import remove
import search_book
import update
import view_all_books

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Search")
    print("4. Update")
    print("5. Remove")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books()
    elif menu == "3":
        search_book.search_book()
    elif menu == "4":
        update.update()
    elif menu == "5":
        remove.remove()
    else :
        print("invalid number")