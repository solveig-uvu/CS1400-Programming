import sys

def growthCalculations(population:int, rate:int, time:int) -> list:
    resultList = []
    resultList.append(population)
    for hr in range(time + 1): # Using the growth calculation to append to the list. Adds an hour since hour 0 is supposed to be the starting population.
        growth = rate * population * (1 - population)
        resultList.append(growth)
        population = growth
    return resultList

# Writing helper functions to extract arguments.
def extractFloat(argument:str) -> float:
    try:
        result = float(sys.argv[argument])
        return result
    except ValueError:
        print(f"Error: Provided argument {argument} is not a float.")
        sys.exit(1)

def extractInt(argument:str) -> int:
    try:
        result = int(sys.argv[argument])
        return result
    except ValueError:
        print(f"Error: Provided argument {argument} is not an integer.")
        sys.exit(1)

# A helper function for writing to the file.
def writeToFile(file:str, iterations:int, list:list):
        if file.endswith('.txt'):
            writer = open(file, 'w')
            for num in range(iterations + 1):
                writer.write(f'{num}\t{list[num]:.3f}\n')
        else:
            fileName = file + '.txt'
            writer = open(fileName, 'w')
            for num in range(iterations + 1):
                writer.write(f'{num}\t{list[num]:.3f}\n')


def main():
    # Ensures whether or not the correct number of arguments are provided.
    if len(sys.argv) != 5:
        print("Usage: python3 gaiaGrowthSimulator.py <initial_population_percentage> <growth_rate> <num_iterations> <output_file>")
        sys.exit(1)

    # Extracting arguments:
    populationPercentage = extractFloat(1)
    growthRate = extractFloat(2)
    numIterations = extractInt(3)
    outputFile = sys.argv[4]

    if 0 < populationPercentage < 1:
        if 0 < growthRate < 4:
            calculatedGrowth = growthCalculations(populationPercentage, growthRate, numIterations)
            writeToFile(outputFile, numIterations, calculatedGrowth)
        else: 
            print("Error: Growth rate must be between 0 and 4.")
    else:
        print("Error: Population percentage must be between 0.1 and 1.")

if __name__ == '__main__':
    main()


'''

============================================================
SELF-EVALUATION (Required)
============================================================

1. ( 15 / 15 points) Writes output to file, formatted correctly with 3 decimal places

2. ( 15 / 15 points) Works with any valid parameter input

3. ( 15 / 15 points) Uses for or while loops, if statements, and user-defined functions

4. ( 5 / 5 points) Code is in a file named gaia_growth_simulator.py

5. ( 5 / 5 points) Contains a main() function with conditional execution

6. ( 10 / 10 points) The Logistic Equation is implemented in its own function

7. ( 10 / 10 points) Correctly parses command line arguments and validates input

8. ( 10 / 10 points) Uses a list to capture all population values over time

9. ( 10 / 10 points) Validates that values are within acceptable ranges

10. ( 5 / 5 points) Follows proper code style (snake_case, variable naming)

Total (100/ 100 points)

============================================================

'''