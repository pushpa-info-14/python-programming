"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such
that every character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both "a"s from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
"""


def min_window(s: str, t: str) -> str:
    if t == "":
        return ""

    count_t, window = {}, {}

    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)

    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = (r - l + 1)
            # pop from left of our window
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l: r + 1] if res_len != float("infinity") else ""


print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
print(min_window("a", "aa"))
