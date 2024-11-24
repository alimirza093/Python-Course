num = int(input("Enter a Number\n"))

if num < 2:
    print("Number is Not Prime")
else:
    is_prime = True
    for i in range(2 , num):
        if num % i  == 0:
            is_prime = False
            break
if is_prime:
    print("Number is Prime")
else:            
    print("Number is Not Prime")