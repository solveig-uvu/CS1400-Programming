# Input validation and conditional formatting for user inputs.
try:
    itemPrice = float(input("Enter the item price: ")) ; 
    userType = input("Enter buyer type ('s' for student, 'f' for faculty): ") ;  # String validation and checking whether the buyer is a student or faculty member.
    if ('s' in userType.lower()): # If the user is a student:
        print(f"Final price after a 5% discount: {itemPrice - ((5 / 100) * itemPrice):.2f}")
    elif ('f' in userType.lower()): 
        print(f"Final price after a 8% discount: {itemPrice - ((8 / 100) * itemPrice):.2f}")
    elif (userType.isdigit() == True): # Checking if the user's input had any digits or not.
        print("Invalid input! The input given was not a character.")
    else:
        print("Invalid input! The user is neither student or faculty.")
except ValueError:
    print("Invalid input! The input given was not numerical.")