userQuit = False

while userQuit == False:
    userCheck = input("Enter an option; 'c' to continue, 'q' to quit.: ")
    if ('c' in userCheck.lower()) and len(userCheck) == 1: # Checking the length of user's input and checking if the input is C.
        try: 
            numberCheck = int(input("Enter a number: ")) ; 
            if numberCheck % 2 == 0: # Checking if the number is even.
                print(f"{numberCheck} is even.")
            else:
                print(f"{numberCheck} is odd.")
        except ValueError: # Input validation error.
            print("Invalid input! The input given was not a number.")
    elif ('q' in userCheck.lower()) and len(userCheck) == 1:
        print("Program terminated.")
        userQuit = True
    else:
        print("Invalid input! Input given must be 'c' or 'q'.")