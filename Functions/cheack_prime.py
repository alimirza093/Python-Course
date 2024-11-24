def is_Prime(num):
    if num == 1 or num == 0:
        return True
    else:
        for i in range(num):
            if num % i == 0:
                return False
            else:
                return True

num = 16
if is_Prime is True:
    print(num,"is Prime")
else:
    print(num,"is not Prime")
