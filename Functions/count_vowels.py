def countVowels(str):
    count = 0
    str = str.lower()
    for val in str:
        if val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u':
                count += 1
    return count


st = "Ali"

print("Number of vowels in given string are",countVowels(st))