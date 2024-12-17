import json

wordlist = {}

while True:
  swedish = input("write a word in Swedish: ").lower()
  if swedish == "":
    break
  english = input("English translation: ").lower()

  wordlist[swedish] = english #whats between the squars is the key, and whats after "=" is the value in the dictionary

with open("dictionary.json", "w", encoding="utf-8")as f:
  json.dump(wordlist, f)