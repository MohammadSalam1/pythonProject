def calculate_level_and_remaining_points(score):

  player_level = score // 100
  player_points = score % 100
  
  return (player_level, player_points)



print(calculate_level_and_remaining_points(250)) # Output: (2, 50)
print(calculate_level_and_remaining_points(435)) # Output: (4, 35)