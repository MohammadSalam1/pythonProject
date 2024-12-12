from datetime import datetime, timedelta

def spring_start_date(temp):
    # Check if the list has fewer than 7 temperatures
    if len(temp) < 7:
        raise ValueError("Minst sju dygnsmedeltemperaturer behövs")
    
    # Define the start and end dates
    start_date = datetime(2024, 2, 15).date()
    end_date = datetime(2024, 7, 31).date()
    
    # Iterate over the temperature list
    for i in range(len(temp) - 6):
        # Check if there are 7 consecutive days with temperatures above 0°C
        if all(temp_val > 0.0 for temp_val in temp[i:i+7]):
            spring_date = start_date + timedelta(days=i)
            
            # Ensure the spring date is not later than the end date
            if spring_date > end_date:
                raise ValueError("Vårens ankomst kan inte vara senare än 31 juli")
            
            return spring_date
    
    # Raise an error if no valid streak is found
    raise ValueError("Våren är inte här än")