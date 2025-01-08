def repeat_characters(word):
    for i, j in enumerate(word, start=1):
        print(j * i, end="")

    return word

print(repeat_characters("ABC")) #Output: ABBCCC
print(repeat_characters("Sweden")) #Output: Swweeeddddeeeeennnnnn
