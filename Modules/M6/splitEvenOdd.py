import re 
# I thought I would learn a little bit of RegEx in order to validate input, if that's not up to specifications I can redo this assignment.

def splitEvenOdd(numbers:list):
    evens = []
    odds = []
    for num in numbers:
        if num % 2 == 0: # Using modulo to figure out whether or not the number in sequence is even or not, and appending said number to the dedicated value list depending on the case.
            evens.append(num)
        else:
            odds.append(num)
    print(f"Original list: {numbers}")
    print(f"Odd values: {odds}")
    print(f"Even values: {evens}")

def main():
    while True:
        userList = input("Enter integers separated by spaces: ")
        if re.search('[a-zA-Z]', userList):
            print("Invalid input! Your list must use integers only.")
            continue
        else:
            userNumbers = [int(i) for i in userList.split()] # Using a for loop to directly add each user input into a list.
            splitEvenOdd(userNumbers)
            break


if __name__ == '__main__':
    main()