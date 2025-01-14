def generate_acronym(sentence):
  new_word = sentence.split()
  ancrynom = ""

  for word in new_word:
    ancrynom += word[0].upper() + "."


  return ancrynom[:-1]


print(generate_acronym("central processing unit"))  # Output: C.P.U 
print(generate_acronym("As soon as possible"))      # Output: A.S.A.P