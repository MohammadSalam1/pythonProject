def update_stock(stock_dict, sales_dict):
  for product, sold_quantity in sales_dict.items():
     if product in stock_dict:
      stock_dict[product] -= sold_quantity
      if stock_dict[product] < 0:
        stock_dict[product] = 0

  return stock_dict

stock = {'apple': 50, 'banana': 30, 'orange': 20}
sales = {'apple': 10, 'banana': 5, 'orange': 25}

print(update_stock(stock, sales))
#output: {'apple': 40, 'banana': 25, 'orange': 0}