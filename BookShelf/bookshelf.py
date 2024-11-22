#opens an empty bookshelf
bookShelf = []

#adds book to the shelf, title is a tring, author is also a string but it is an opetional parameter.
def add_book (title, author="Unknown"):
  book = { #book entery
    "title": title,
    "author": author
  }

  #use append to add books
  bookShelf.append(book)
#confirmation to the user that it added the book
  print(f"Book {title}, author {author} added to the bookshelf") 

#display books in the list
def display_books ():
  if not bookShelf: #checks if the shelf is empyt
    print("the book shelf is empty")
  else: #if the shelf is not empyt
    print("\nthe books are:") #print \n on a new line

    #sets idx (index) for the books from 1 for easier recollection, enumerate generates the book name and the index
    for idx, book in enumerate(bookShelf, start=1): 
      print(f"{idx}. {book["title"]} by {book["author"]}")#prints index of the book, book title and author.
  

#to withdraw books
def draw_book(title):
    for book in bookShelf:  # will go through the list of books
        if book["title"].lower() == title.lower():  # checks if the book is in the shelf
            bookShelf.remove(book)  # if the book is in, it's removed and a message is printed
            print(f"The book '{title}' has been withdrawn.")
            return  # stops after removing the book
    
    # If the loop finishes without finding the book
    print(f"Error: The book '{title}' is not found on the shelf.")
    if bookShelf:  # If there are books in the shelf
        print("Available books on the shelf:")
        display_books()  # Call the existing display_books function to list the books
    else:
        print("The bookshelf is currently empty.")
