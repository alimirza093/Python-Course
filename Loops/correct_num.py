guessNo = 70


userNo = int(input("Guess The Number\n"))

while userNo != guessNo:
    if userNo > guessNo:
        print("Please Enter a small Number\n")
    elif userNo < guessNo:
        print("Please Enter a large Number\n")

    userNo = int(input("Guess Number Again\n"))
    
print("Number Guessed Successfully\n")


