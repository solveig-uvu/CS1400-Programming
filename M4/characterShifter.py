def shiftCharacter(char, shift, mode):
    if len(char) != 1:
        print("Invalid input! You used more than one character.")
    else:
        if mode in ('forward', 'plus', '+'): # Handles the mode if it is forward.
            shift = abs(shift)
        elif mode in ('backward', 'minus', '-'): # Handles the mode if it is backward.
            shift = -shift
        else:
            print("Invalid input! You must either use forward, backwards, plus or minus or their signs.")
            
        if 'a' <= char <= 'z': # Handles lowercase characters.
            asciiOffset = ord('a')
            newPosition = (ord(char) - asciiOffset + shift) % 26
            newChar = chr(newPosition + asciiOffset)
            return newChar
        elif 'A' <= char <= 'Z': # Handles uppercase characters.
            asciiOffset = ord('A')
            newPosition = (ord(char) - asciiOffset + shift) % 26
            newChar = chr(newPosition + asciiOffset)
            return newChar
        else: # Handles special or numerical characters.
            print("You used a non-alphabetical character!")
            return char

# Defining the main function.
def main():
    userChar = input("Enter a character: ")
    userChar = userChar.strip()
    try: 
        userShift = int(input("Enter a shift value: ")) ; 
        userMode = input("Enter a mode (forward, backward): ")
        userMode = userMode.strip().lower()
        shiftedCharacter = shiftCharacter(userChar, userShift, userMode)
        print(f'Shifted character: {shiftedCharacter}')
    except ValueError: # Checks for if the user is inputting a number or not, raises an error if its not.
        print("Invalid input! You must use a whole number for the shift value.")

main()