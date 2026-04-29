valUserName = input("What is your full name? ")

# Checks if the user ID is 8 numbers long
while True:
    valUserID = input("What is your UVU ID? ")
    if len(valUserID) != 8:
        print("Invalid length. Your UVU ID must be 8 numbers long.")
    else: # Checks if the user ID can be converted into an integer, if not it will raise an exception
         try:
             checkUserID = int(valUserID) ; break
         except ValueError:
             print("Invalid input! Your UVU ID must be written with numbers.")

print("Hello " + valUserName + ", your UVU ID is " + valUserID + "!")