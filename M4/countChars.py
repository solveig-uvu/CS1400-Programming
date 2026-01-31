# Defining a function that counts the amount of times a character appears in the string sequence. 
def characterCounter(input,char):
    numFound = 0
    for ch in input.lower():
        if ch == char.lower(): numFound += 1
    return numFound

# The main function that gathers user input and calls the characterCounter function. Strips whitespace from user input to ensure no whitestring is in there.
def main():
    userString = input('Enter a string: ')
    cleanString = userString.strip()
    userCharacter = input('Enter a character to count: ')
    cleanCharacter = userCharacter.strip()
    return print(f"The character '{cleanCharacter}' appears {characterCounter(cleanString, cleanCharacter)} times in '{cleanString}'.")

main()
        