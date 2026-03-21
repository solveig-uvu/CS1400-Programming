import random

# Creating a helper function to generate the tuple the user will be guessing the combination from.
def generateCombination() -> tuple:
    numbers = tuple(random.randint(1, 20) for _ in range(5))
    return numbers

def getUserGuess(msg:str) -> tuple:
    userInput = input(msg).split(' ')
    userGuess = tuple(userInput)
    return userGuess

# Game function for checking the user's guess against the generated tuple.
def guessCheck(guess:tuple, answer:tuple) -> int:
    correctGuesses = 0
    index = 0
    for num in range(len(answer)):
        if int(guess[index]) == answer[index]:
            correctGuesses += 1
        index += 1
    return correctGuesses

# Helper function for the attempt counter and main game functionality.
def attemptCounter(numAttempts:int=5, answerCombo:tuple=(1,2,3,4,5)) -> int:
    attempt = 1
    attemptGuesses = []
    userWon = False
    while attempt <= numAttempts:
        userGuess = getUserGuess(f'Attempt {attempt}: Enter 5 numbers: ')
        numGuessed = guessCheck(userGuess, answerCombo)
        if numGuessed != 5:
            print(f'{numGuessed} number(s) matched in the correct position.')
            attempt += 1
            attemptGuesses.append(numGuessed)
        else:
            print('You guessed correctly!')
            userWon = True
            break
    if userWon != True:
        bestMatch = int(100 * (max(attemptGuesses) / len(answerCombo)))
        print(f"Sorry! The correct combination was {answerCombo}.")
        print(f"Your best match was {bestMatch}%.")        
    else:
        print(f"You guessed correctly in {attempt} attempt(s).")

def main():
    combo = generateCombination()
    attemptCounter(5,combo)

if __name__ == '__main__':
    main()