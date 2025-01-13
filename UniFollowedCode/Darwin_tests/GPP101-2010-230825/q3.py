def final_position(directions):
  x = 0
  y = 0

  for i in directions:
    if i == "N":
      y += 1
    elif i == "S":
      y -= 1
    elif i == "E":
      x += 1
    elif i == "W":
      x -= 1

  return (x, y)




print(final_position("NS"))           # Output: (0, 0) 
print(final_position("NESW"))         # Output: (0, 0) 
print(final_position("NEESNW"))        # Output: (1, 1) 
print(final_position("SSWWNEEE"))     # Output: (1, -1)