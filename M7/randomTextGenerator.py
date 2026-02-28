import random
import sys
seed = random.seed(3123920)

def makeWord() -> str:
    alphabet = tuple('abcdefghijklmnopqrstuvwxyz')
    word = ''
    wordLength = random.randint(5,10) # Using random.randint() to generate the numbers specified to create random words.
    for char in range(wordLength):
        pulledCharacter = random.randint(1, 26) - 1
        word = word + alphabet[pulledCharacter]
    return word

def makeLine() -> str:
    lineText = ''
    lineLength = random.randint(8, 10)
    for word in range(lineLength):
        newWord = makeWord()
        lineText = lineText + f'{newWord} '
    lineText = lineText.strip()
    return lineText

# The writer function. If there's no arguments passed, it will automatically create a text document with 100 lines.
def writeRandomText(lines=100):
    try: 
        lines = int(lines) ; 
        writer = open('output.txt', 'w')
        for num in range(lines - 1):
            currentLine = makeLine()
            writer.write(f'{currentLine}\n')
        lastLine = makeLine()
        writer.write(f'{lastLine}')
    except ValueError:
        print("Error: You must use an integer when providing a desired document length amount.")

# Helper function for extracting the desired document length from command line arguments.
def extractInt(argument:str) -> int:
    try:
        result = int(sys.argv[argument]) ; return result
    except ValueError:
        print(f"Error: Provided argument {argument} is not an integer.")
        sys.exit(1)    

def main():
    # Ensures whether or not the correct number of arguments are provided.
    if len(sys.argv) >= 3:
        print("Usage: python randomTextGenerator.py [document_length]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        docLength = extractInt(1)
        writeRandomText(docLength)
    else:
        writeRandomText()

if __name__ == '__main__':
    main()