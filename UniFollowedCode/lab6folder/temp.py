import json

#Open the JSON file for reading
with open("sweden_temperatures.json", "r+") as f:
    #Load the existing data from the JSON file
    data = json.load(f)

#Get user input for the month and temperature
month = input("Enter month name: ").capitalize()
temp = int(input("Enter temperature: "))

#Check if the new temperature is higher than the existing record
if temp > data.get(month):
    #Update the record
    data[month] = temp

    #Write the updated data back to the file
    with open("sweden_temperatures.json", "w+") as f:
        json.dump(data, f)  # Write updated data with formatting

    #Notify the user
    print("Record updated successfully!")
else:
    #Notify the user that no update is needed
    print("No update needed.")




