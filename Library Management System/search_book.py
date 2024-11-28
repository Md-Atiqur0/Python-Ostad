import csv

def search_book():
    print("Which one want to use for search book? Title / ISBN Number")
    print("Type 1 for Title OR Type Any Number for ISBN Number")
    chose = int(input("Enter Number : "))
    if chose == 1:
        title = input("Enter Book title: ")
        with open("all_books.csv", "r") as fp:
            for row in csv.reader(fp):
                if title == row[0]:
                    print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")
                    break
                else:
                    print("Book Not Found")
    '''else:
        isbn = input("Enter ISBN Number: ")
        with open("all_books.csv", "r") as fp:
            for row in csv.reader(fp):
                if isbn == row[2]:
                    print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")
                else:
                    print("Book Not Found")'''