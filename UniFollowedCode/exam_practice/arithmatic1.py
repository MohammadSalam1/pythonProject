def calculate_saving_time(total_amount, daily_saving):

    days = total_amount // daily_saving
    remaining_amount = total_amount % daily_saving
    hours = (remaining_amount / daily_saving) * 24
    return int(days), int(hours)
    
print(calculate_saving_time(250, 10))  
print(calculate_saving_time(365, 15)) 
print(calculate_saving_time(100, 7)) 
