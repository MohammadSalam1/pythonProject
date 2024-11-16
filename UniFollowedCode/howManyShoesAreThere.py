# Som ni redan vet har alla mina skor samma färg, storlek och modell. Varje högersko kan
# alltså paras ihop med vilken vänstersko som helst och vice versa. I förra laborationen
# skrev ni ett program som läser in antalet vänsterskor och antalet högerskor från
# användaren. Programmet beräknade och skrev ut antalet kompletta par och antalet
# överblivna skor. Dessvärre kunde den utskrivna texten bli lite konstig, med fel former
# av vissa ord.

# I den här uppgiften ska utskriften snyggas till så att programmet
#   * väljer rätt form: överbliven/överblivna, sko/skor
#   * anger om de överblivna skorna är högerskor eller vänsterskor
#   * anpassar texten om inga skor blivit över

# Exempel 1: (Talen 8 och 5 anges av användaren)
# Hur många vänsterskor finns det? 8
# Hur många högerskor finns det? 5
# Det finns 5 par och 3 överblivna vänsterskor.

# Exempel 2: (Talen 1 och 32 anges av användaren)
# Hur många vänsterskor finns det? 25
# Hur många högerskor finns det? 26
# Det finns 25 par och 1 överbliven högersko.

# Exempel 3: (Talen 17 och 17 anges av användaren)
# Hur många vänsterskor finns det? 17
# Hur många högerskor finns det? 17
# Det finns 17 par och inga överblivna skor.

# Läs in antal vänsterskor och gör om till heltal
left_shoes = int(input("How many left side shoes? "))

# Läs in antal högerskor och gör om till heltal
right_shoes = int(input("How many right side shoes? "))

# Beräkna antal kompletta par
both_shoes = min(left_shoes, right_shoes)

# Beräkna antal överblivna skor
leftovers = abs(left_shoes - right_shoes)

# Write out the results
if leftovers > 0:
    # check if its right or left side
    if left_shoes > right_shoes:
        leftover_shoes = "vänsterskor"
        #if only one shoe left
        if leftovers == 1:
            leftover_form = "överbliven" #use singular form
        else:
            leftover_form = "överblivna" #use plural form (more than one shoe)
    elif right_shoes > left_shoes:
        leftover_shoes = "högerskor" #sets the left over type to right shoes
        
        #check again if there is one shoe left
        if leftovers == 1:
            leftover_form = "överbliven"
        else:
            leftover_form = "överblivna"
    #if there is no shoes left
    else:
        leftover_shoes = ""  # This shouldn't be used if the shoes are equal
        leftover_form = ""   # In case of equal, we don’t need leftover shoes description

    # Singular/plural for "sko/skor"
    if leftovers == 1:
        shoe_form = "sko"
    else:
        shoe_form = "skor"
    
    # Print the result
    print(f"Det finns {both_shoes} par och {leftovers} {leftover_form} {shoe_form} ({leftover_shoes}).")
else:
    # Case when there are no leftovers
    print(f"Det finns {both_shoes} par och inga överblivna skor.")
