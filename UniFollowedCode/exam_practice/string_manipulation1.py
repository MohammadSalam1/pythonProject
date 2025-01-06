def reverse_each_word(sentence):
    sentence = sentence.split()
    reversed_words = []
    
    for word in sentence:
        reversed_words.append(word[::-1])
    
    return ' '.join(reversed_words)
    
    
print(reverse_each_word("Hello World"))          # Expected Output: "olleH dlroW"
print(reverse_each_word("Python programming"))  # Expected Output: "nohtyP gnimmargorp"
print(reverse_each_word("This is fun"))         # Expected Output: "sihT si nuf"

