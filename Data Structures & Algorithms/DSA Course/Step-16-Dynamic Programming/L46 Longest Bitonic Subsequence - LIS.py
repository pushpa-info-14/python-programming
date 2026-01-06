"""
https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688

A Bitonic Sequence is a sequence of numbers that is first strictly increasing and then strictly decreasing.

A strictly ascending order sequence is also considered bitonic, with the decreasing part as empty, and
same for a strictly descending order sequence.

For example, the sequences [1, 3, 5, 3, 2], [1, 2, 3, 4] are bitonic, whereas the sequences [5, 4, 1, 4, 5]
and [1, 2, 2, 3] are not.

You are given an array 'arr' consisting of 'n' positive integers.

Find the length of the longest bitonic subsequence of 'arr'.

Example :
Input: 'arr' = [1, 2, 1, 2, 1]

Output: 3

Explanation: The longest bitonic subsequence for this array will be [1, 2, 1]. Please note that [1, 2, 2, 1] is
not a valid bitonic subsequence, because the consecutive 2's are neither strictly increasing, nor strictly decreasing.
"""

from typing import List


def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    dp1 = [1] * n
    dp2 = [1] * n

    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and dp1[i] < 1 + dp1[prev]:
                dp1[i] = 1 + dp1[prev]
    for i in range(n - 1, -1, -1):
        for prev in range(i + 1, n):
            if arr[prev] < arr[i] and dp2[i] < 1 + dp2[prev]:
                dp2[i] = 1 + dp2[prev]
    res = 0
    for i in range(n):
        res = max(res, dp1[i] + dp2[i] - 1)

    return res


print(longestBitonicSubsequence([1, 2, 1, 2, 1], 5))
print(longestBitonicSubsequence([1, 2, 1, 3, 4], 5))
