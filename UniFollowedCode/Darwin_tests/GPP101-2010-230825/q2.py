def calculate_discount(total_spending):
  if total_spending <= 100:
    return 0
  elif total_spending <= 500:
    return total_spending * 0.05
  elif total_spending <= 1000:
    return total_spending * 0.1
  elif total_spending > 1000:
    return total_spending * 0.15

print(calculate_discount(50))    # Output: 0 
print(calculate_discount(150))   # Output: 7.5 
print(calculate_discount(600))   # Output: 60.0 
print(calculate_discount(1200))  # Output: 180.0