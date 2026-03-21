# Helper function for gathering user input.
def askNum(message:str) -> int:
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except ValueError:
            print("Invalid input! You must use an integer.")
            continue

# Creating the list all the values and steps will be sorted into.
def createList(startVal:int, stepVal:int, endVal:int) -> list:
    stepCount = endVal / stepVal
    newVal = startVal + stepVal
    finalList = [startVal, newVal]
    for num in range(int(stepCount - 1)):
        newVal += stepVal
        finalList.append(newVal)
    return finalList

# Creating the file handler.
def createFile(numList:list) -> None:
    writer = open('numberSeries.txt', 'w')
    for num in range(len(numList) - 1):
        writer.write(f'{numList[num]}\n')
    writer.write(f'{numList[-1]}')
    print(f'Saved {len(numList)} numbers to numberSeries.txt')

def main():
    startingNum = askNum("Enter starting number: ")
    endingNum = askNum("Enter ending number: ")
    stepSize = askNum("Enter step size: ")
    numSeries = createList(startingNum,stepSize,endingNum)
    createFile(numSeries)

if __name__ == '__main__':
    main()