def remove_short_strings(string_list):
  result = []
  for string in string_list:
    if len(string) >= 5:
      result.append(string)

  return result




# Test case 1 
words1 = ["apple", "banana", "grape", "kiwi", "pear", "orange"] 
print(remove_short_strings(words1))  # Output: ["apple", "banana", "orange", "grape"] 
 
# Test case 2 
words3 = ["python", "java", "c++", "ruby", "swift"] 
print(remove_short_strings(words3))  # Output: ["python", "swift"]