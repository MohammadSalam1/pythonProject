def calculate_bmi_category(height, weight):
  bmi = weight // (height ** 2)

  if bmi < 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  elif bmi > 30:
    return "Obesity"
  
  return bmi


print(calculate_bmi_category(1.75, 70)) # Output:  Normal weight 
print(calculate_bmi_category(1.8, 89))  # Output:  Overweight