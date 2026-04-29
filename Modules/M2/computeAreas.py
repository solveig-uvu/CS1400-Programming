import math

try:
    usrRadius = float(input("Enter the circle's radius: ")) ; print(f"The area of the circle entered is {math.pi * (usrRadius ** 2):.4f}")
except ValueError:
    print("Invalid input! Use only a numerical value for the circle's radius.")


# Nesting a try/catch block within another one in order to calculate the rectangle's area.
try: 
    usrWidth = float(input("Enter the width of the rectangle: ")) ; 
    try: 
        usrHeight1 = float(input("Enter the height of the rectangle: ")) ; print(f"The area of the rectangle is {usrWidth * usrHeight1:.4f}")
    except ValueError:
        print("Invalid input! The height of the rectangle must be numerical.")
except ValueError:
    print("Invalid input! The width of the rectangle must be numerical.")

# Doing the same as above for input validation. If the user's input can't be validated it will skip the attempt to calculate the area in full.
try:
    usrBase = float(input("Enter the base of the triangle: ")) ;
    try:
        usrHeight2 = float(input("Enter the height of the triangle: ")) ; print(f"The area of the triangle is {(usrBase * usrHeight2) / 2:.4f}")
    except ValueError:
        print("Invalid input! The height of the triangle must be numerical.")
except ValueError:
    print("Invalid input! The base of the triangle must be numerical.")
