def ageCheck(message:str) -> int:
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Invalid input! You must use a number for your age.")
            continue
        else:
            if 0 < userInput < 120: # Checks if the user is in between 1 and 119 years old.
                return userInput
            else:
                print("Invalid input! Age must be older than 0, and younger than 120.")
                continue

def nameCheck(message:str) -> str:
    while True:
        userInput = input(message)
        if userInput.isalpha():
            return userInput.capitalize()
        else:
            print("Invalid input! You must use characters only inputting your name.")
            continue

def main():
    userName = nameCheck("Enter your name: ")
    userAge = ageCheck("Enter your age: ")
    print(f"Thanks, {userName}! Your age is {userAge}.")

main()