# Setting up the encoding / decoding function.
def cipherShifter(input, key, mode):
    if mode in ('e', 'encrypt'):
        key = abs(key)
    elif mode in ('d', 'decrypt'):
        key = -abs(key)
    else:
        print("Invalid input! Your mode must either be (e)ncrypt, or (d)ecrypt.")

    textResult = ""
    for ch in input:
        # This for loop will individually go every single character listed in the text input and encode or decode accordingly.
        if 'a' <= ch <= 'z':
            # Handles lowercase.
            asciiOffset = ord('a')
            newPos = (ord(ch) - asciiOffset + key) % 26
            ch = chr(newPos + asciiOffset)
        elif 'A' <= ch <= 'Z':
            # Handles uppercase.
            asciiOffset = ord('A')
            newPos = (ord(ch) - asciiOffset + key) % 26
            ch = chr(newPos + asciiOffset)
        # Other characters (numbers, spaces, punctuation) will automatically be unchanged.

        textResult += ch
    return textResult

def userContRequest():
    cont = input("Would you like to continue encoding / decoding? ((q)uit, (c)ontinue): ")
    if cont in ('continue', 'y', 'c'):
        return True
    elif cont in ('quit', 'n', 'q'):
        return False
    else:
        print("Invalid input! You must either specify whether you want to (c)ontinue or (q)uit.")
        return 'Repeat'
    
# Defining the main function. Will run on a while loop for as long as the user wishes to continue.
def main():
    userContinue = True
    while userContinue == True:
        userContinue = userContRequest()
        if userContinue == 'Repeat':
            userContinue = True
            continue
        elif userContinue == False:
            break
        else:
            userInput = input("Enter the message: ")
            userInput = userInput.strip()
            userMode = input("Enter your mode; (e)ncode or (d)ecode: ")
            userMode = userMode.strip()
            try:
                userKey = int(input("Enter the message's key: ")) ; 
                if userMode in ('e', 'encrypt'): 
                    print(f"Encrypted message: {cipherShifter(userInput, userKey, userMode)}")
                elif userMode in ('d', 'decrypt'):
                    print(f'Decrypted message: {cipherShifter(userInput, userKey, userMode)}')
                else:
                    cipherShifter(userInput, userKey, userMode)
            except ValueError:
                print("Invalid input! You must enter a whole integer.")


main()


'''

============================================================
SELF-EVALUATION (Required)
============================================================
1. ( 30 / 30 points) The program works with the given text and ciphering shown in the Sample Input and Output

2. ( 30 / 30 points) The program works with different unknown texts and ciphers, not just the Sample Input and Output

3. ( 30 / 20 points) The program contains loops (for and while), if statements, and user-defined functions to organize code 

4. ( 10 / 10 points) The program contains a main function with conditional execution; no global code

5. ( 10 / 10 points) All variable names and the code follow Python snake case or camelCase 

Total (100 / 100 points)

============================================================

'''