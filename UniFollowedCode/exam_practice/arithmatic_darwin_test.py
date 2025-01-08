def calculate_popcorn_cost_in_sek(grams):
  total_cost = grams * 0.20

  cost_in_kr = int(total_cost)

  ore_left = int((total_cost - cost_in_kr)*100)

  return (cost_in_kr, ore_left)

print(calculate_popcorn_cost_in_sek(750)) # Output: (150, 0)
print(calculate_popcorn_cost_in_sek(76)) # Output: (15, 20)