import bookshelf

def main():
  myBooks = bookshelf.bookShelf
  while True:
    #display the menu
    print("\n Welcome to our booksehlf")
    print("1. Add a book ")
    print("2. Withdraw a book ")
    print("3. Display book list ")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    #takes in choice
    if choice == 1:
      title = input("Enter the book title: ")
      author = input("Enter the author (optional): ")
      bookshelf.add_book(title, author)
    elif choice == 2:
      title = input("What book do you wish to withdraw: ")
      bookshelf.draw_book()
    elif choice == 3:
      bookshelf.display_books()
    elif choice == 4:
      print("See you soon")
      break
    else:
      print("Invalid Choice, please try again")

if __name__ == "__main__":
    main()