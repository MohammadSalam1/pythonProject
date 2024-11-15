#take input of how many eggs from the user
num_eggs = int(input("egg count: "))

#use division to count all eggs
num_boxes = num_eggs // 6

#modulu will give you the rest or number of eggs left
eggs_left = num_eggs % 6

#results
print(f"eggs you put in are {num_eggs} which fit in {num_boxes} boxes. you would have {eggs_left} leftover")