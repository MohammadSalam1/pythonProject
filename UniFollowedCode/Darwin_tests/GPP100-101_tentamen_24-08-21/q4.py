def remove_divisibles(lst, d):
  new_lst = []

  for num in lst:
    if num % d != 0:
      new_lst.append(num)
  return new_lst


lst = [2, 4, 5, 10, 15, 20]
d = 5
result = remove_divisibles(lst, d)
print(result) #output: [2, 4]