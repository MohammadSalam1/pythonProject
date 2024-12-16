filename = input("give me a txt file path:")
word = input("word to find: ")

with open(filename, encoding="utf-8") as f:
  content = f.read()

for i, line in enumerate(content):
  if word in line:
    print(i, line)
