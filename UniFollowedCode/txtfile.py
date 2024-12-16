file_name = input("enter file name: ")

with open(file_name) as f:
  content = f.readlines()

print(content)