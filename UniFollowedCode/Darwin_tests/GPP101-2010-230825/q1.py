def feeding_status(hours_since_last_meal):
  bitpets = hours_since_last_meal
  if bitpets <= 4:
    return "Full"
  elif bitpets <= 5:
    return "Hungry"
  elif bitpets > 5:
    return "Unhappy"
  

print(feeding_status(2))   # Output: "Full" 
print(feeding_status(4))   # Output: "Full" 
print(feeding_status(4.5)) # Output: "Hungry" 
print(feeding_status(6))   # Output: "Unhappy"