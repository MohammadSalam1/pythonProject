def calculate_bmi_category(height, weight):
  bmi = weight / (height **2)
  height = 0
  weight = 0

  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal Weight"
  elif bmi <= 29.9:
    return "Overweight"
  else:
    return "Obesity"
  


print(calculate_bmi_category(1.75, 70)) # Output: Normal weight
print(calculate_bmi_category(1.8, 89)) # Output: Overweight