#A delivery company must load packages for delivery in a car. The car has a maximum load it can take and the packages have different weights. 
#The packages must be packed in the order they arrive, without exceeding the maximum load.
#Write a program that reads in a maximum load and weight per package.
#The user enters packages as long as the maximum load is not exceeded.
#Save the code in a file named paket.py.
    #skeleton plan:
#make a program to check the weight of a package befoer it is delivered
#create an input variable to decide the max weight to transfer
#create a loop to keep asking for weights
#create an if statement talking to check if the input weight is what accepted
#let the weight add to the one before and save it
#break the loop once the weight limit is reached
#make sure to add an error message if the weight is exceeded.

#take the weight of the transfer from the user
max_load = int(input("Ange maxvikt "))

#set a starting weight
current_load_weight = 0
package_count = 0

#loop to add the package
while True:
  #take the package weight off the user and add to package_weight
  package_weight = int(input("Paketets vikt "))

  #if statement to check if the weight has exceeded the max_load
  if current_load_weight + package_weight > max_load:
    break #this to break the while loop otherwise it'll continue repeating nonstop

  current_load_weight += package_weight
  package_count += 1

  #print(f"package added. Current total weight: {current_load_weight}") #tells the user how much weight they have added

print(f"Du kan lasta {package_count} paket. Totalvikten är {current_load_weight} kg.")