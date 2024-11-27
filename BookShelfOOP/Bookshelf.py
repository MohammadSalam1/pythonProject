class Bookshelf:
    def __init__(self):
        self.books = [] 
        
    def addbooks(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        if not author.strip():
            author = "unknown"
        self.books.append({"Title": title, "Author": author})
        print(f"The book you added: '{title}' written by {author}.")
    
    def removebooks(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book['Title'].lower() == title_to_remove.lower():
                self.books.remove(book)
                print(f"The book '{book['Title']}' by {book['Author']} has been removed.")
                return
        print("Book not found. No book removed.")
        
    def displaybooks(self):
        if not self.books:
            print("The bookshelf is empty.")
        else:
            print("Books on the shelf are: ")
            for book in self.books:
                print(f"- {book['Title']} by {book['Author']}")    
  

# Create a bookshelf object
#my_shelf = Bookshelf()

# Add books interactively
#my_shelf.addbooks()
#my_shelf.addbooks()

#my_shelf.displaybooks()

# remove books
#my_shelf.removebooks()
#display books
#my_shelf.displaybooks()