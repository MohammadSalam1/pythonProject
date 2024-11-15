dollar_price = float(input("how much do you want to put in? "))
kr_per_dollar = float(input("kr per dollar: "))
#convert the prices from dollar to kroner
kronor_price = dollar_price * kr_per_dollar

#:.2f will give an appoximatoin of the price to the closest two decimal points.
print(f"approximated price in kronor {kronor_price:.2f}") 