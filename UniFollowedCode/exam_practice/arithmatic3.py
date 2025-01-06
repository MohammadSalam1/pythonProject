def calculate_work_time(total_hours, daily_hours, break_hours):
    effective_daily_hours = daily_hours - break_hours
    days_to_finish = total_hours // effective_daily_hours
    remaining_hours = total_hours % effective_daily_hours

    
    return int(days_to_finish), int(remaining_hours)
    
    
    
print(calculate_work_time(50, 8, 1))  # Expected Output: (7, 0)
print(calculate_work_time(100, 6, 2))  # Expected Output: (14, 2)
print(calculate_work_time(72, 9, 1))  # Expected Output: (8, 0)