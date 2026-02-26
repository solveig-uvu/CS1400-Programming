from math import pi
from math import tan

def areaRegularPentagon(lengthSide:int) -> float:
    area = (5 * (lengthSide ** 2)) / (4 * tan(pi/5))
    return float(area) # This function is just used to calculate the area of a pentagon using tangent and pi. 

def areaMultiplePentagons(numPentagons:int, lengthSide:int) -> float: 
    pentagonArea = areaRegularPentagon(lengthSide)
    area = numPentagons * pentagonArea
    return float(area)

def main():
    try:
        numPentagons = int(input("No. of Pentagons: ")) ; 
        try:
            if numPentagons >= 1: 
                lengthSides = int(input("Side Length of each pentagon: ")) ; 
                if lengthSides >= 1:
                    areaPentagons = areaMultiplePentagons(numPentagons, lengthSides)
                    print(f"Total area for {numPentagons} with a side length of {lengthSides}: {areaPentagons:.4f}")
                else:
                    print("Invalid input! You did not use a positive integer.")
            else:
                print("Invalid input! You did not use a positive integer.")
        except ValueError:
            print("Invalid input! You must use an integer when inputting the side length.")
    except ValueError:
        print("Invalid input! You must use an integer when inputting the number of pentagons.")

main()