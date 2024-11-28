from save_books import save_books

def add_books(all_books):
    title = str(input("Enter Book Title: "))
    author = str(input("Enter Author Name: "))
    isbn = input("Enter ISBN Number: ")
    year = int(input("Enter Publishing year Number: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))


    book  = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }

    all_books.append(book)
    save_books(all_books)

    print("Books Added Successully")
    all_books.clear()
    return all_books