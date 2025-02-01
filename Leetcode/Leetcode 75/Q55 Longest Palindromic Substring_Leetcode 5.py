"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.



Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


def longest_palindrome(s: str) -> str:
    def check_palindrome(s, l, r, res, res_len):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r + 1]
                res_len = r - l + 1
            l -= 1
            r += 1
        return res, res_len

    res = ""
    res_len = 0
    for i in range(len(s)):
        # odd length
        res, res_len = check_palindrome(s, i, i, res, res_len)
        # even length
        res, res_len = check_palindrome(s, i, i + 1, res, res_len)

    return res


print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
