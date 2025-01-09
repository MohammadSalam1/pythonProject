def feeding_status(hours_since_last_meal):
  
  if hours_since_last_meal <= 4:
        return "Full"
  elif 4 < hours_since_last_meal <= 5:
        return "Hungry"
  else:
        return "Unhappy"



print(feeding_status(2)) # Output: "Full"
print(feeding_status(4)) # Output: "Full"
print(feeding_status(4.5)) # Output: "Hungry"
print(feeding_status(6)) # Output: "Unhappy"