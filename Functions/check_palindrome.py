def checkPalindrome(str):
    str = str.lower()
    left = 0
    right = len(str) - 1
    is_palindrome = True
    while left < right:
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1
    return is_palindrome

st = "POp"

if checkPalindrome(st) == True:
    print("Given String is Palindrome")
else:
    print("Given String is not Palindrome")
    