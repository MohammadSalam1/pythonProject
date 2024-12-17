import json

with open("wordlist.json", "r") as f:
  wordlist = json.load(f)

while True:
  
  swedish = input("write a Swedish word: ").lower()
  if swedish == "":
    break
  english = input("English translation").lower()
  wordlist[swedish] = english

  with open("wordlist.json", "w") as f:
    json.dumb(wordlist, f)