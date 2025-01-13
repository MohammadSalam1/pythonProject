def feet_inches(inches):
  feet = inches // 12
  inches = inches % 12

  return (feet, inches)

print(feet_inches(27)) # (2, 3)
print(feet_inches(93)) # (7, 9)