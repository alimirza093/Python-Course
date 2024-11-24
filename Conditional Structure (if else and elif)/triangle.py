side1 = float(input("Enter the length of the first side: \n"))
side2 = float(input("Enter the length of the second side: \n"))
side3 = float(input("Enter the length of the third side: \n"))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The lengths entered cannot form a triangle.")
