def center_list(lst):
  mean = sum(lst) // len(lst)
  
  for i in range(len(lst)):
    lst[i] -= mean

  return mean

values = [12, 5, 9, 13, 11]
avg = center_list(values)
print(avg) # 10.0
print(values) # [2.0, -5.0, -1.0, 3.0, 1.0]