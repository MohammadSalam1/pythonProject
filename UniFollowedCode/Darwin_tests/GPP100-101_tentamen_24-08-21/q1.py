def calculate_popcorn_cost_in_sek (grams):
  full_cost = grams * 0.20

  price_kr = int(full_cost)
  left_ore = int((full_cost - price_kr) * 100)

  return (price_kr, left_ore)


print(calculate_popcorn_cost_in_sek(750))  # Output: (150, 0) 
print(calculate_popcorn_cost_in_sek(76))  # Output: (15, 20)