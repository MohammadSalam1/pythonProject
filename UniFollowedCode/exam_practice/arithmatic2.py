def calculate_filling_time(tank_capacity, fill_rate, initial_water):
    # Calculate the number of full hours needed
    hours = (tank_capacity - initial_water) // fill_rate
    # Calculate the remaining liters and convert to minutes
    remaining_liters = (tank_capacity - initial_water) % fill_rate
    minutes = (remaining_liters / fill_rate) * 60
    # Return the result as a tuple
    return int(hours), int(minutes)

# Test cases
print(calculate_filling_time(1000, 50, 200))  # Expected: (16, 0)
print(calculate_filling_time(750, 45, 100))  # Expected: (14, 26)
print(calculate_filling_time(500, 60, 100))  # Expected: (6, 40)
