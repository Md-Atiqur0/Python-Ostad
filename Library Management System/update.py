import csv

def update():
    print("Which one want to Update? Price / Quantity Number")
    print("Type 1 for price OR Type Any Number for Quantity Number")
    chose = int(input("Enter Number : "))
    if chose == 1:
        with open("all_books.csv","r") as fp:
            li = []
            isbn = input("Enter Book ISBN For Update: ")
            for row in csv.reader(fp):
                if row[2] == isbn:
                    new_price = input("Enter the Update price of Book: ")
                    row[4] = new_price
            li.append(row)
        with open("all_books.csv","w+",newline="") as fp:
            writer=csv.writer(fp)
            writer.writerows(li)
            print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")
    else:
        with open("all_books.csv", "r") as fp:
            li = []
            isbn = input("Enter Book ISBN For Update: ")
            for row in csv.reader(fp):
                if row[2] == isbn:
                    new_quantity = input("Enter the Update Number of Quantity: ")
                    row[5] = new_quantity
            li.append(row)
        with open("all_books.csv", "w+", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerows(li)
            print(f"Title: {row[0]} | Author: {row[1]} | ISBN: {row[2]} | Year: {row[3]} | Price: {row[4]} | Quantity: {row[5]}\n")


