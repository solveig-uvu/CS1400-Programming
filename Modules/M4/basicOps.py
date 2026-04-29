# Defining basic arithmetic functions. 

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Invalid input! You cannot divide with or by zero.")
        return 0 # Handles dividing by zero. Will print an error if that is attempted.'
    else:
        return num1 / num2

# Defining functions to ask the user for number inputs.
def getNumber1():
    try:
        userNum = int(input("Enter the first number: ")) ; return userNum
    except TypeError:
        print("Invalid input! You must use an integer.")
        return 0

def getNumber2():
    try:
        userNum = int(input("Enter the first number: ")) ; return userNum
    except TypeError:
        print("Invalid input! You must use an integer.")
        return 0


# Defining the main function. Will use a loop to repeatedly use this basic calculator.
def main():
    userContinue = True
    while userContinue == True:
        userOperation = input('Enter the operation (+, -, *, /, all, q, you may use arithmetic terms such as add or divide.): ')
        if userOperation.lower() in ('q', 'quit'): # If statements to decide what the user wishes to use for operations.
            userContinue = False
        elif userOperation.lower() in ('+', 'add', 'addition'):
            userNum1 = getNumber1()
            userNum2 = getNumber2()
            print(f"{userNum1} + {userNum2} = {addition(userNum1, userNum2)}")
        elif userOperation.lower() in ('-', 'subtract', 'subtraction'):
            userNum1 = getNumber1()
            userNum2 = getNumber2()
            print(f"{userNum1} - {userNum2} = {subtraction(userNum1, userNum2)}")
        elif userOperation.lower() in ('*', 'multiply', 'multiplication'):
            userNum1 = getNumber1()
            userNum2 = getNumber2()
            print(f"{userNum1} * {userNum2} = {multiplication(userNum1, userNum2)}")
        elif userOperation.lower() in ('/', 'divide', 'division'):
            userNum1 = getNumber1()
            userNum2 = getNumber2()
            print(f"{userNum1} / {userNum2} = {division(userNum1, userNum2)}")
        elif userOperation.lower() == 'all':
            userNum1 = getNumber1()
            userNum2 = getNumber2()
            print(f"Addition: {addition(userNum1, userNum2)}")
            print(f"Subtraction: {subtraction(userNum1, userNum2)}")
            print(f"Multiplication: {multiplication(userNum1, userNum2)}")
            print(f"Division: {division(userNum1, userNum2)}")
        else:
            print("Invalid input! Please try again using the keywords listed.")

main()