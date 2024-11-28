
def save_books(all_books):
    with open("all_books.csv","a",newline="") as fp:
        for book in all_books:
            line = f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']},\n"
            fp.write(line)
        #writer = csv.writer(fp)
        #writer.writerow(all_boo ks)