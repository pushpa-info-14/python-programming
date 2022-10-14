def valid_palindrome(s: str):
    s = ''.join([i.lower() for i in s if i.isalpha() or i.isnumeric()])
    left, right = 0, len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(valid_palindrome("A man, a plan, a canal: Panama"))
    print(valid_palindrome("race a car"))
    print(valid_palindrome(" "))
    print(valid_palindrome("0P"))
