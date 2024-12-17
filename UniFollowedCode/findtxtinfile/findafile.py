filename = input("give me a txt file path:")
word = input("word to find: ")

with open('hello.txt') as f:
  content = f.readlines()

new_content = []
for i, line in enumerate(content):
  if word in line:
    new_content.append(str(i) + " " + line)

new_filename = filename + word + ".txt"

with open(new_filename, "w", encoding="utf-8") as f:
  f.writelines(new_content)
