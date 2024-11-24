def factorial(num):
    if num < 0:
        raise ValueError("Factorial of Negative Numbers is not Exist")
    elif num == 0 or num == 1:
        return 1
    else:
            return num * factorial(num - 1)


print("Factorial =",factorial(5)); 