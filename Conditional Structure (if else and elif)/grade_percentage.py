marks = int(input("Enter marks out of 100\n"))

if marks > 80 and marks <= 100:
    print("You got A Grade")

elif marks > 70 and marks <= 80:
    print("You got B Grade")

elif marks > 60 and marks <= 70:
    print("You got C Grade")
    
elif marks > 50 and marks <= 60:
    print("You got D Grade")

else:
    print("You are failed")
