# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

def search_book_title(book, title):
    if title in book:
        return book[title]
    else:
        return "Book not found "


all_books = {

    "Sev Hacy" : " Axel Bakunts " ,
    "Garibaldiakany" : " Avetik Isahakyan" ,
    "Hay Muky" : " William Saroyan" ,
}

search = "Abu Lala Mahari"
print(search_book_title(all_books , search))
