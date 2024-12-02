def is_pangram(text):
    # Definiera det engelska alfabetet (utan å, ä, ö)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Konvertera texten till små bokstäver så att vi hanterar både stora och små bokstäver
    text = text.lower()
    
    # Skapa en mängd för att hålla reda på de bokstäver som finns i texten
    found_letters = set()
    
    # Loopa genom varje tecken i texten
    for char in text:
        # Om tecknet är en bokstav och finns i alfabetet, lägg till det i mängden
        if char in alphabet:
            found_letters.add(char)
        
        # Om alla bokstäver har hittats, kan vi direkt returnera True
        if len(found_letters) == len(alphabet):
            return True
    
    # Om vi har gått igenom hela texten utan att hitta alla bokstäver, returnera False
    return False

# Exempel på användning
print(is_pangram("The quick brown fox jumps over the lazy dog."))  # Förväntas: True
print(is_pangram("Hello World!"))  # Förväntas: False
