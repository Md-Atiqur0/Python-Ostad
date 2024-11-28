import csv

def remove():
    with open("all_books.csv", "r") as fp:
        li = []
        isbn = input("Enter Book ISBN For Delete: ")
        for row in csv.reader(fp):
            if row[2] == isbn:
                print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")
                print("This Book is Deleted")
            else:
                li.append(row)
    with open("all_books.csv", "w+", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerows(li)
        print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")