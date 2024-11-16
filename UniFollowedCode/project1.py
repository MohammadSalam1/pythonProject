#project one. kickstart my journey.
#let's make a small calculator for no
#try to comment more to help future self and others
fstnum = int(input("chose your first number: ")) #asks user for integer (digit)
scdnum = int(input("chose your second number: ")) #asks for a second number
gv_answer = input("choose [add, subtract, multiply, divide]: ") #asks user for what arithmetic function they want

if gv_answer == "add": #adds inputs
    rslt = fstnum + scdnum
    print(rslt) #shows results

if gv_answer == "subtract": #subtracts inputs
    rslt = fstnum - scdnum
    print(rslt)

if gv_answer == "multiply": #multiplys inputs
    rslt = fstnum * scdnum
    print(rslt)

if gv_answer == "divide": #divides inputs
    rslt = fstnum / scdnum
    print(rslt)
