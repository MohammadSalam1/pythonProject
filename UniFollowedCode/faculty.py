#take a num from user
n = int(input("n: "))

n_faculty = 1

#(start, stop, range. so 1 is the desired start value, n is the final value wanted and +1 the steps you want the program to take)
for i in range(1, n, +1):
  print(i)
  n_faculty *= i #takes the number before and multiplying with the next.

print("n!: ", n_faculty)