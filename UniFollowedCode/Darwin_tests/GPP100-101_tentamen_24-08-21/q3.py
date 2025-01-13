def repeat_characters(word):
    results = ""
    for i, j in enumerate(word, start=1):
        results += j * i 

    return results

print(repeat_characters("ABC")) #Output: ABBCCC
print(repeat_characters("Sweden")) #Output: Swweeeddddeeeeennnnnn
