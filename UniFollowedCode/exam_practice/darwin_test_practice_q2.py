def calculate_rental_cost (days):
  if days == 1:
    price = 40
  elif days <= 5:
    price = 35
  elif days <= 10:
    price = 30
  else:
    price = 25
  
  return price * days

print(calculate_rental_cost(2)) # Output: (70)
print(calculate_rental_cost(4)) # Output: (140)
print(calculate_rental_cost(12)) # Output: (300)