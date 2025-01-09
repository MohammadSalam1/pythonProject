def remove_divisibles(lst, d):
  
  modified_lst = [x for x in lst if x % d != 0]
  
  
  return modified_lst if len(modified_lst) != len(lst) else lst

lst = [2, 4, 5, 10, 15, 20]
d = 5
result = remove_divisibles(lst, d)
print(result) # Output: [2, 4]