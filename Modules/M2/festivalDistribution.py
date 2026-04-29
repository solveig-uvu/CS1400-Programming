import math

# Gathering user input for ration calculation
numColonists = int(input("How many colonists are there celebrating the festival? "))
availableUnits = float(input("How much total food rations are available in units? "))

# Creating new variables to store the calculated ration allocation and remaining rations.
rationAllocation = 4 * numColonists
remainingRations = availableUnits - rationAllocation

# Calculating the cuts from Zerin and Lyra, after the festival's cuts before going to the colonists.
zerinShare = (15 / 100) * remainingRations
print(zerinShare)
remainingRations = remainingRations - zerinShare
lyraShare = (10 / 100) * remainingRations
print(lyraShare)
remainingRations = remainingRations - lyraShare
equalShare = remainingRations / numColonists
print(equalShare)
zerinTotal = equalShare + zerinShare + 4
lyraTotal = equalShare + lyraShare + 4 

# Printing the logistics of the original supply, how many rations were used, and how many are remaining, formatted using 2 decimal places.
print(f"The original ration supply was {availableUnits:.2f}.")
print(f"The festival allocated {rationAllocation:.2f} rations, with 4 units per colonist.")
print(f"Zerin's share was {zerinTotal:.2f}, while Lyra's was {lyraTotal:.2f}.")
print(f"The remaining rations for each colonist is {equalShare + 4:.2f}.")