def is_palindrome(input_string):
  input_string = input_string.lower()
  word = []

  for char in input_string:
    if char.isalnum():
      word.append(char)

  return word == word[::-1]


print(is_palindrome("Racecar"))          # Expected Output: True
print(is_palindrome("hello"))            # Expected Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Expected Output: True
