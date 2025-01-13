def calculate_level_and_remaining_points(score):
  level = score // 100
  remaining_score = score % 100

  return(level, remaining_score)


print(calculate_level_and_remaining_points(250))   # Output:  (2, 50)
print(calculate_level_and_remaining_points(435))   # Output:  (4, 35)