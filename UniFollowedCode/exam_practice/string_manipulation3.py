def count_vowels(input_string):
    input_string = input_string.lower()
    vowel = ["a", "e", "i", "o", "u"]
    vowel_num = 0
    
    for char in input_string:
        if char in vowel:
            vowel_num += 1

        
    return vowel_num
    
    
    
print(count_vowels("Hello World"))      # Expected Output: 3
print(count_vowels("PYTHON programming"))  # Expected Output: 4
print(count_vowels("Giraffe"))          # Expected Output: 3