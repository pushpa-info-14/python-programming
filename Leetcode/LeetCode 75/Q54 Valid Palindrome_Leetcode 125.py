"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""


def is_palindrome1(s: str) -> bool:
    new_str = ""

    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


def is_palindrome2(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not is_alpha_num(s[l]):
            l += 1
        while l < r and not is_alpha_num(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def is_alpha_num(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


print(is_palindrome1("A man, a plan, a canal: Panama"))
print(is_palindrome1("race a car"))
print(is_palindrome1(" "))
print(is_palindrome2("A man, a plan, a canal: Panama"))
print(is_palindrome2("race a car"))
print(is_palindrome2(" "))
