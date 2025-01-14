def calculate_seasonal_averages(temperature_data):
  seasonal_average = []

  for season in temperature_data:
    average = sum(season) / len(season)
    seasonal_average.append(round(average, 1))

  return seasonal_average




temperature_matrix = [[25, 28, 23], [30, 35, 28], [22, 20, 25], [27, 30, 29]] 
print(calculate_seasonal_averages(temperature_matrix)) 
# Output: [25.3, 31.0, 22.3, 28.7] 
 
temperature_matrix = [[15, 18, 21], [27, 31, 35], [33, 31, 25], [20, 15, 10]] 
print(calculate_seasonal_averages(temperature_matrix)) 
# Output: [18.0, 31.0, 29.7, 15.0]