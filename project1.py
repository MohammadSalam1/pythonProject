#project one. kickstart my journey.
#let's make a small calculator for no
fstnum = int(input("chose your first number: "))
scdnum = int(input("chose your second number: "))
rslt = float()
gv_answer = input("choose [add, subtract, multiply, divide]: ")

if gv_answer == "add":
    rslt = fstnum + scdnum
    print(rslt)

if gv_answer == "subtract":
    rslt = fstnum - scdnum
    print(rslt)

if gv_answer == "multiply":
    rslt = fstnum * scdnum
    print(rslt)

if gv_answer == "divide":
    rslt = fstnum / scdnum
    print(rslt)
