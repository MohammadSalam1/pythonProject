def generate_email(full_name):
  names = full_name.split()
  first_name = names[0]
  last_name = names[1]

  first_part = first_name[:2]
  last_part = last_name[-2:]

  email = first_part + last_part + "@example.com"

  return email



print(generate_email("John Doe")) #Output: Jooe@example.com
print(generate_email("Alex Turner")) #Output: Aler@example.com