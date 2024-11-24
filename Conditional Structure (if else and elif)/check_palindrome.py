str = input("Enter a string\n")

str.replace(" " , "").lower()

left = 0
right = len(str) - 1

is_palindrome = True

while left < right:
    if str[left] != str[right]:
        is_palindrome = False
        break
    else:
        left += 1
        right -= 1

if is_palindrome == True:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome")

