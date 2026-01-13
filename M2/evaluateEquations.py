eq1Case1 = (10 - 3) * 4
eq1Case2 = 10 - (3 * 4)

print("Equation: 10 - 3 * 4")
print(f"Case 1: (10 - 3) * 4 = {eq1Case1}")
print(f"Case 2: 10 - (3 * 4) = {eq1Case2}")

# Switching the parenthesis will change which side is calculated first. In case 2, instead of adding 30 to 4 right away, it will add 30 after 4 is divided by 2.
eq2Case1 = (30 + 4) / 2
eq2Case2 = 30 + (4 / 2)

print("Equation: 30 + 2 / 4")
print(f"Case 1: (30 + 2) / 4 = {eq2Case1}")
print(f"Case 2: 30 + (4 / 2) = {eq2Case2}")

eq3Case1 = 24 + (40 ** 3)
eq3Case2 = (24 + 40) ** 3
 
print("Equation: 24 + 40 ** 3")
print(f"Case 1: 24 + (40 ** 3) = {eq3Case1}")
print(f"Case 2: (24 + 40) ** 3 = {eq3Case2}")