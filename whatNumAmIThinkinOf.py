import random

secretnm = random.randint(1, 10)

print("guess what number am I thinking of!")

while True:
  guess = int(input("? "))
  if guess == secretnm:
    print("you guessed right")
    break
  elif guess < secretnm:
    print("your guess is too low")
  else:
    print("guess is too high")
    
  