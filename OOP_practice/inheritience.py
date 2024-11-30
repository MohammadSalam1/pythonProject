class Student:
    def __init__(self, name):
        self.__name = name  # Private name attribute
        self.__grade = []   # Private grade list attribute
  
    def getName(self):
        return self.__name  # Getter for name
    
    def setNewName(self, newName):
        self.__name = newName  # Setter for name

    def getGrade(self):
        try:
            grade = float(input("Enter a grade (0 - 100): "))
            if 0 <= grade <= 100:
                self.__grade.append(grade)  # Append valid grade to the grade list
                print(f"Grade {grade} added.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a number.")
    
    def displayGrade(self):
        """Display all grades."""
        if self.__grade:
            print(f"Grades for {self.__name}: {self.__grade}")
        else:
            print(f"No grades available for {self.__name}.")

    def averageGrade(self):
        """Calculate and return the average grade."""
        if self.__grade:
            avg = sum(self.__grade) / len(self.__grade)
            return avg
        else:
            return None

# Function to display the menu and interact with the user
def main_menu(student):
    while True:
        # Display the menu options
        print("\nChoose an option:")
        print("1. Add grade")
        print("2. Show average grade")
        print("3. Display grades")
        print("4. Exit")

        # Get user input
        choice = input("Enter your choice: ")

        # Perform actions based on user input
        if choice == "1":
            student.getGrade()  # Call the getGrade method
        elif choice == "2":
            avg = student.averageGrade()  # Call averageGrade method
            if avg is not None:
                print(f"The average grade for {student.getName()} is {avg:.2f}.")
            else:
                print(f"No grades available for {student.getName()}.")
        elif choice == "3":
            student.displayGrade()  # Call the displayGrade method
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please choose a valid option.")

# Main part of the program
student_name = input("Enter student's name: ")
student = Student(student_name)

# Start the menu loop
main_menu(student)

class Person:
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address