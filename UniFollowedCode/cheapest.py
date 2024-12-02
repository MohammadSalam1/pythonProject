def cheapest_3h (number):
  min_sum = float('inf')
  mix_index = -1
  
  for i in range (0, len(number)-2):
    results = number[i] + number[i+1] + number[i+2]
    print(f"index{i}")

    if results < min_sum:
        min_sum = results
        min_index = i
  return min_index
  
