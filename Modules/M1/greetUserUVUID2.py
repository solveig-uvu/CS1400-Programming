usrName = input("What is your full name? ")

# Gets user ID.
usrID = input("What is your UVU ID? ")

# Checks user ID for being numerical and if it is 8 characters long, if not it will raise an exception / error message.
if len(usrID) != 8:
    print("Invalid input! The ID entered is not 8 characters.")
else:
    try:
        checkUsrID = int(usrID) ; print(f"Hello {usrName}! Your UVU ID is {usrID}.")
    except ValueError:
        print("Invalid input! The ID given is not numerical.")