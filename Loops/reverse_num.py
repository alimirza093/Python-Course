num = input("Enter a Number\n")

num_list = list(num)
left = 0
right = len(num_list) - 1

while left < right:
    num_list[left] , num_list[right] = num_list[right] , num_list[left]
    left += 1
    right -= 1 

reversed_string = ''.join(num_list)
print("Reverse Number: ",reversed_string)