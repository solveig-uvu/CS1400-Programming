while True:
    userInput = input("Enter a word to encode: ")
    if userInput.isdigit(): # Validating whether or not the user's input has any digits.
        print("Invalid input! Input must be a word.")
        continue
    else:
        try:
            shiftValue = int(input("Enter a shift value: ")) ; 

            newWord = ""
            for ch in userInput.lower():
                if 'a' <= ch <= 'z':
                    asciiOffset = ord('a')
                    newValue = (ord(ch) - asciiOffset + shiftValue) % 26
                    ch = chr(newValue + asciiOffset)                  
                    newWord += ch
            # The new position is calculated by the ASCII offset of the letter 'A' minus the Character's ASCII code and adding the shift value to it, and adding the remainder to the ASCII code of 'A'.
            print(f"Encoded word is {newWord}!")

                
        except ValueError:
            print("Invalid input! Input must be numerical.")
