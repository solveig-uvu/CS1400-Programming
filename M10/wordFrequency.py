def wordCount(text:str='The game is the best way to the best heart.') -> dict:
    counter = {}
    words = text.split()
    for word in words:
        if word not in counter:
            counter[word.lower()] = 1
        else:
            counter[word.lower()] += 1
    return counter

def main():
    print("Original Word Frequencies:")
    words = wordCount()
    moreThanOne = words.copy()
    for key in words:
        value = words[key]
        if moreThanOne[key] <= 1:
            moreThanOne.pop(key)
        print(f"{key}: {value}")
    print("After removing words with only one occurance:")
    for key in moreThanOne:
        value = moreThanOne[key]
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()