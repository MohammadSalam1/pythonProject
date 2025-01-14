def calculate_discounted_price(original_price_sek):
  price = original_price_sek

  if price <= 50:
    return price
  elif price <= 500:
    return price - (price * 0.1)
  elif price <= 1000:
    return price - (price * 0.3)
  
  return price
  





print(calculate_discounted_price(40)) #Output: 40
print(calculate_discounted_price(100)) #Output: 90
print(calculate_discounted_price(520)) #Output: 346
print(calculate_discounted_price(1000)) #Output: 700

