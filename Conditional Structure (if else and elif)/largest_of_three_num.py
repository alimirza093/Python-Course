x = int(input("Enter first number\n"))
y = int(input("Enter second number\n"))
z = int(input("Enter third number\n"))
if x > y and  x > z:
    max_num = x
elif y > z:
    max_num = y
else:
    max_num = z

print("Maximum Number is",max_num)
    