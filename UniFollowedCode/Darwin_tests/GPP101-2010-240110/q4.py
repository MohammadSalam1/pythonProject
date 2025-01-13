def find_common_elements(list1, list2):
  common_numbers = []
  for element in list1:
    if element in list2:
      common_numbers.append(element)

  return common_numbers



print(find_common_elements([1, 2, 3, 4, 5], [3, 5, 7, 9]))   
# Output: [3, 5] 
 
print(find_common_elements([4, 7, 2, 9, 1], [12, 1, 4, 3,7]))   
# Output: [4, 7, 1]