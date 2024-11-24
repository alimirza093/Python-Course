temperature = float(input("Enter Temperature in Celcius\n"))

if temperature <= 0:
    print("It's Freezing")
elif temperature > 0 and temperature <= 25:
    print("Temperature is Moderate")
else:
    print("It's Hot")
    