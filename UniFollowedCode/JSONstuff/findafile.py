filename = input("give me a txt file path:")
word = input("word to find: ")

with open('hello.txt', encoding="utf-8") as f:
  content = f.readlines()

for i, line in enumerate(content):
  if word in line:
    print(i, line)
