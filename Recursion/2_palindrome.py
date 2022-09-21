def palindrome(s):
    l = len(s)
    if l < 2:
        return True
    elif s[0] == s[- 1]:
        return palindrome(s[1: - 1])
    else:
        return False


string = input('Enter Input : ')

if palindrome(string):
    print(f"'{string}' is palindrome")
else:
    print(f"'{string}' is not palindrome")
