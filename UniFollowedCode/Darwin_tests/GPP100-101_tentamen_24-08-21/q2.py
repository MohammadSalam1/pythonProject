def calculate_rental_cost (days):
  if days <= 1:
    return 40 * days
  elif days <= 5:
    return 35 * days
  elif days <= 10:
    return 30 * days
  elif days > 10:
    return 25 * days
  




print(calculate_rental_cost(2))  # Output: (70) 
print(calculate_rental_cost(4))  # Output: (140) 
print(calculate_rental_cost(12)) # Output: (300)