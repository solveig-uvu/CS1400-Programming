# Vowel counter function, it'll go through the words given for each line and count vowels. I'm unsure if Y counts as a vowel in this assignment or not since to the best of my knowledge it is not, but just to be safe I will count that too.

def countVowels(file:str) -> list:
    vowelCounts = [0, 0, 0, 0, 0, 0]
    try: 
        reader = open(file, 'r')
        for line in reader:
            for char in line.lower():
                if 'a' in char:
                    vowelCounts[0] += 1
                elif 'e' in char:
                    vowelCounts[1] += 1
                elif 'i' in char:
                    vowelCounts[2] += 1
                elif 'o' in char:
                    vowelCounts[3] += 1
                elif 'u' in char:
                    vowelCounts[4] += 1
                elif 'y' in char:
                    vowelCounts[5] += 1
        return vowelCounts
    except IOError:
        print(f"Error: Could not open file {file}")
        return vowelCounts


# Asking for the filename to count vowels from helper function. Will automatically default to 'sampleText.txt' if no input is provided.
def askFileName() -> str:
    fileName = input("What is the file you would like to input? ").strip()
    if fileName.endswith('.txt'):
        return fileName
    elif fileName == '':
        fileName = 'sampleText.txt'
        return fileName
    else:
        newFile = fileName + ".txt"
        return newFile
    
def printCounts(vowels:list):
    totalVowels = sum(vowels)
    print(f"There were {vowels[0]} a's, {vowels[1]} e's, {vowels[2]} i's, {vowels[3]} o's, {vowels[4]} u's, and {vowels[5]} y's, totalling at {totalVowels} vowels.")

def main():
    fileName = askFileName()
    vowelsInFile = countVowels(fileName)
    printCounts(vowelsInFile)

if __name__ == '__main__':
    main()
