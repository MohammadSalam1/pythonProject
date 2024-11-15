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
def draw_book (title, author="Unknown"):
  for book in bookShelf: #will go through the list of books
    if book["title"].lower() == title.lower(): #cheks what book is in the shelf (book list)
      bookShelf.remove(book) #if the book is in then its removed and printed 
      print(f"book{title} has been withdrawn")
      return #stops
    print(f"book{title} is not found on the shelf") #if book not found then it tells so

