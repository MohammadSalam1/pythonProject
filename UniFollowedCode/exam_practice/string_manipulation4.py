def reverse_each_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Initialize an empty list to store reversed words
    reversed_words = []
    # Reverse each word and append it to the list
    for word in words:
        reversed_words.append(word[::-1])
    # Join the reversed words into a single string with spaces
    return ' '.join(reversed_words)

# Test cases
print(reverse_each_word("Hello World"))          # Expected Output: "olleH dlroW"
print(reverse_each_word("Python programming"))  # Expected Output: "nohtyP gnimmargorp"
print(reverse_each_word("This is fun"))         # Expected Output: "sihT si nuf"
