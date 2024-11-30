#def starts the func, greet is the name of it, (name) are the parameters
# def greet(name):
#   print(f"hello {name}") #what the code should do [code block]

# user_name = input("what is your name?") #takes input from user
# greet(user_name)#call the function called greet and put the input in it to run it


# def avg(a, b):
#   return (a + b) / 2

# x = int(input("chose a nm "))
# y = int(input("chose a nm "))
# res = avg(x, y) #passing x for a and y for b
# print(f"the average of x, y is {res}")

def swap(a, b):
  a, b = b, a

x = 2
y = 6
swap(x, y)
print(f"x = {x} and y = {y}")