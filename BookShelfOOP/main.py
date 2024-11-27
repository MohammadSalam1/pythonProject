from Bookshelf import Bookshelf  # Import the Bookshelf class from bookshelf.py

# Create a bookshelf object
my_shelf = Bookshelf()

def main_menu():
    while True:
        # Display the menu options
        print("\nChoose an option:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Display Books")
        print("4. Exit")

        # Get user input
        choice = input("Enter your choice: ")

        # Perform actions based on user input
        if choice == "1":
            my_shelf.addbooks()  # Call the addbooks method
        elif choice == "2":
            my_shelf.removebooks()  # Call the removebooks method (acting as borrow for now)
        elif choice == "3":
            my_shelf.displaybooks()  # Call the displaybooks method
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the menu
if __name__ == "__main__":
    main_menu()
