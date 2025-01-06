def calculate_fuel_efficiency(distance_traveled, fuel_used, distance_to_travel):
    fuel_efficiency = distance_traveled / fuel_used
    liters_needed = distance_to_travel / fuel_efficiency
    return fuel_efficiency, liters_needed
    
print(calculate_fuel_efficiency(500, 25, 200))  # Expected Output: (20.0, 10.0)
print(calculate_fuel_efficiency(300, 15, 450))  # Expected Output: (20.0, 22.5)
print(calculate_fuel_efficiency(600, 40, 300))  # Expected Output: (15.0, 20.0)