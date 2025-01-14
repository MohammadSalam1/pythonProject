def calculate_sales_difference(sales_figures):
  average = sum(sales_figures) // len(sales_figures)

  results = []

  for sale in sales_figures:
    results.append(sale - average)

  return results





print(calculate_sales_difference([900, 1200, 1300, 1000, 600]))
# Output: [-100, 200, 300, 0, -400]
print(calculate_sales_difference([35, 100, 45]))
# Output: [-25, 40, -15]