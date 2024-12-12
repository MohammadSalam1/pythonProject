from season_tools import spring_start_date

def main():
    # Prompt the user for input
    user_input = input("Enter daily average temperatures with spaces: ")
    
    # Convert the input into a list of floats
    try:
        temp_list = [float(x) for x in user_input.split()]
    except ValueError:
        print("This is not a number, please enter valid temperatures.")
        return
    
    # Call the spring_start_date function and handle errors
    try:
        results = spring_start_date(temp_list)
        print(f"Vårens ankomst: {results}")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()