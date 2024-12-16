import sys

f = open('fruit.txt', mode='r', encoding="utf-8")
for row in f:
  print(row, end='')
f.close()