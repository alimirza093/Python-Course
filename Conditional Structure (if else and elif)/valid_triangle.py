sideOne = int(input("Enter first side\n"))
sideTwo = int(input("Enter second side\n"))
sideThree = int(input("Enter third side\n"))

if (sideOne + sideTwo > sideThree) and (sideOne + sideThree > sideTwo) and (sideTwo + sideThree > sideOne):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
