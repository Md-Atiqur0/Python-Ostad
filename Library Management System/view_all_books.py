import csv

def view_all_books():
    with open("all_books.csv","r") as fp:
        for book in csv.reader(fp):
            print(f"Title: {book[0]} | Author: {book[1]} | ISBN: {book[2]} | Year: {book[3]} | Price: {book[4]} | Quantity: {book[5]}\n")

