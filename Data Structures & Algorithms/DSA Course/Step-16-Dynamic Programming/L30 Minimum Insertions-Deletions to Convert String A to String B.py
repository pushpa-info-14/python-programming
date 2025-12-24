def canYouMake(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return m + n - 2 * dp[m][n]


# deletions = m - len(lcs)
# insertions = n - len(lcs)
# res = m + n - 2 x len(lcs)
"""
https://www.naukri.com/code360/problems/minimum-number-of-deletions-and-insertions_4244510

You are given 2 non-empty strings 's1' and 's2' consisting of lowercase English alphabets only.

In one operation you can do either of the following on 's1':
(1) Remove a character from any position in 's1'.
(2) Add a character to any position in 's1'.

Find the minimum number of operations required to convert string 's1' into 's2'.

Example:
Input: 's1' = "abcd", 's2' = "anc"

Output: 3

Explanation:
Here, 's1' = "abcd", 's2' = "anc".
In one operation remove 's1[3]', after this operation 's1' becomes "abc".    
In the second operation remove 's1[1]', after this operation 's1' becomes "ac".
In the third operation add 'n' in 's1[1]', after this operation 's1' becomes "anc".

Hence, the minimum operations required will be 3. It can be shown that there's no way to convert s1 into s2 in less than 3 moves.
"""
print(canYouMake("aaa", "aa"))
print(canYouMake("edl", "xcqja"))
