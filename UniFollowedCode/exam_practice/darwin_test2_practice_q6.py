def total_discount_price(item_prices, sold_items):
  total_price = 0

  for item in sold_items:
    if item in item_prices:
      total_price += item_prices[item] * 0.8
      
  return total_price


prices = {'apple': 2, 'banana': 1, 'orange': 1, 'grape': 3, 'kiwi':7}
items_sold1 = ['apple', 'orange', 'kiwi']
items_sold2 = ['banana', 'grape']
items_sold3 = ['orange', 'kiwi']

print(total_discount_price(prices, items_sold1)) # Output: 8.0
print(total_discount_price(prices, items_sold2)) # Output: 3.2
print(total_discount_price(prices, items_sold3)) # Output: 6.4