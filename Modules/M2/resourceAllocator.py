# Calculating the allocation for each citizen, subtracting Mira and Tov.
totalCitizens = int(input("How many citizens are aboard? "))
totalUnits = float(input("How many units are available? "))
citizenAllocation = (totalCitizens - 2) * 3
remainingUnits = totalUnits - citizenAllocation

# Calculating Mira, Tov, and the Crew's shares.
miraShare = (13 / 100) * remainingUnits
remainingUnits = remainingUnits - miraShare
tovShare = (11 / 100) * remainingUnits
remainingUnits = remainingUnits - tovShare
equalShare = remainingUnits / totalCitizens

# Calculating the total taken between Mira, Tov and then each crew member.
miraTotal = equalShare + miraShare
tovTotal = equalShare + tovShare
crewShares = equalShare + 3

# Printing outputs.
print(f"Mira's share: {miraTotal:.2f}")
print(f"Tov's share: {tovTotal:.2f}")
print(f"Crew's share: {equalShare:.2f}")
