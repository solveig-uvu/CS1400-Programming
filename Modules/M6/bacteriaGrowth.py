def growthRate(population:int, rate:float, time:int) -> list:
    resultList = []
    resultList.append(population)
    for hr in range(time + 1): # Using the growth calculation example in the assignment description. Adds an hour since hour 0 is supposed to be the starting population.
        growth = population * rate
        population = growth
        resultList.append(growth)
    return resultList


def main():
    while True: # Input validation. I could've made functions for each one of these if needed.
        try: 
            startingPopulation = int(input("Enter starting population: ")) ; 
            try:
                rate = float(input("Enter hourly growth rate: ")) ; 
                try: 
                    numHours = int(input("Enter amount of hours: ")) ; 
                    calculatedRates = growthRate(startingPopulation, rate, numHours)
                    for hr in range(numHours + 1):
                        print(f"Hour {hr}: {calculatedRates[hr]:.2f}")
                    break
                except ValueError:
                    print("Invalid input! You must use an integer when inputting hours.")
                    continue
            except ValueError:
                print("Invalid input! You must use a float when inputting the growth rate.")
                continue
        except ValueError:
            print("Invalid input! You must use an integer when using a population.")
            continue

if __name__ == '__main__':
    main()