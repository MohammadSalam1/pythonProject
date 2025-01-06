def generate_initials(full_name):
    
    name = full_name.split()
    initials = [word[0].upper() for word in name]
    formated_initials = ".".join(initials)
    return formated_initials
    
print(generate_initials("John Doe"))         # Expected Output: J.D
print(generate_initials("Ada Lovelace"))     # Expected Output: A.L
print(generate_initials("grace hopper"))     # Expected Output: G.H