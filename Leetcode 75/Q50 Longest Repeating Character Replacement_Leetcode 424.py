"""
You are given a string s and an integer k. You can choose any character of the string and change it
to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
"""
import time


def character_replacement1(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


def character_replacement2(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    max_f = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_f = max(max_f, count[s[r]])

        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


print(character_replacement1("ABAB", 2))
print(character_replacement1("AABABBA", 1))
print(character_replacement2("ABAB", 2))
print(character_replacement2("AABABBA", 1))
