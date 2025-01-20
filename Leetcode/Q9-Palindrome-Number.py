def palindrome(x: int):
    s = str(x)
    left, right = 0, len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(palindrome(121))
print(palindrome(2))
print(palindrome(21))
