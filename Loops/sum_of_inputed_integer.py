num = input("Enter a number\n")

num_list = list(num)

sum = 0

for i in range (len(num_list)):
    sum += int(num_list[i])
print("Sum = ",sum)