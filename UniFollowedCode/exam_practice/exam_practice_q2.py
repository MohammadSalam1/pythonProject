def season(month, day):
  if (month == 8 and day >= 18) or (9 <= month <= 11) or (month == 12 and day <= 22):
    return "höst"
  elif (month == 12 and day >= 23) or (month == 1 and day <= 10):
    return "vinter"
  elif (month == 1 and day >= 11) or (2 <= month <= 5) or (month == 6 and day <= 10):
    return "vår"
  elif (month == 6 and day >= 11) or (month == 7):
    return "sommar"




print(season(6, 17)) # sommar
print(season(3, 12))
print(season(7, 19))