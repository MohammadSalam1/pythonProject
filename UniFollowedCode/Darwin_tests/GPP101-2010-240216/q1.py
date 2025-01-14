def calculate_travel_time(distance):
  speed = distance // 60
  minutes = distance % 60

  return (speed, minutes)


print(calculate_travel_time(120)) #output: (2, 0)
print(calculate_travel_time(70)) #output: (1, 10)
print(calculate_travel_time(30)) #output: (0, 30)