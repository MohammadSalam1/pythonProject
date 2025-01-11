def generate_email(full_name):
    # Split the full name into first and last name
    first_name, last_name = full_name.split()
    
    # Extract the required parts
    first_part = first_name[:2].capitalize()  # First two letters of the first name
    last_part = last_name[-2:].lower()       # Last two letters of the last name
    
    # Construct the email
    email = first_part + last_part + "@example.com"
    
    return email

# Test cases
print(generate_email("john Doe"))      # Output: Jooe@example.com
print(generate_email("Alex Turner"))   # Output: Aler@example.com
