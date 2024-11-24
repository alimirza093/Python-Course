num1 = float(input("Enter First Number\n"))
op = input("Enter an Operator\n")
num2 = float(input("Enter Second Number\n"))

if op == '+':
    print(num1 ,"+", num2 , "=",num1+num2)
elif op == '-':
    print(num1 ,"-", num2 , "=",num1-num2)
elif op == '*':
    print(num1 ,"*", num2 , "=",num1+num2)
elif op == '/':
    if num2 == 0:
        print("Can't Divide By Zero\n")
    else:
        print(num1 ,"/", num2 , "=",num1/num2)
else:
    print("Invalid Input")


