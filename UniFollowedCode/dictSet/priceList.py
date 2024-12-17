pricelist = {"apple": 12, "banana": 10, "chocolateball": 7, "daim": 23}
total = 0

while True:
  things = input("what would you like in your bag: ")
  if things == "":
    break
  if things in pricelist:
    total += pricelist[things]
  else:
    print(f"we do not have {things}")
    print("we have: ", pricelist)


print("that will be", total)
