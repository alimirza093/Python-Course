sum_even = 0
sum_odd = 0
sp = int(input("Enter starting point\n"))
ep = int(input("Enter ending point\n"))
for i in range(sp , ep+1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i 
print("Sum of all even numbers from" ,sp, "to" ,ep, "is" ,sum_even,"\n")
print("Sum of all odd numbers from" ,sp, "to" ,ep, "is" ,sum_odd,"\n")