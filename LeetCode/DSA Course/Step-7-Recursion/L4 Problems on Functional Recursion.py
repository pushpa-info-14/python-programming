# Reverse an array
def reverse(i, arr, n):
    if i >= n // 2: return arr
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    reverse(i + 1, arr, n)
    return arr


print(reverse(0, [1, 2, 3], 3))


# Check string is a palindrome
def isPalindrome(s):
    n = len(s)

    def check(i):
        if i >= n // 2: return True
        if s[i] != s[n - 1 - i]: return False
        return check(i + 1)

    return check(0)


print(isPalindrome("aba"))
print(isPalindrome("abba"))
print(isPalindrome("abbc"))
