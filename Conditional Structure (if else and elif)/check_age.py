age = int(input("Enter Your Age\n"))

if age < 18:
    print("You are Minor Citizen")
elif age >= 18 and age < 40:
    print("You are Adult Citizen")
else:
    print("You are Senior Citizen")
