import math

# Gathering user input for ration calculation
numColonists = int(input("How many colonists are there celebrating the festival? "))
availableUnits = float(input("How much total food rations are available in units? "))

# Creating new variables to store the calculated ration allocation and remaining rations.
rationAllocation = 4 * numColonists
remainingRations = availableUnits - rationAllocation

# Printing the logistics of the original supply, how many rations were used, and how many are remaining, formatted using 2 decimal places.
print(f"The original ration supply was {availableUnits:.2f}.")
print(f"The festival allocated {rationAllocation:.2f} rations, with 4 units per colonist.")
print(f"There are now a total of {remainingRations:.2f} rations left for the festival stockpile.")