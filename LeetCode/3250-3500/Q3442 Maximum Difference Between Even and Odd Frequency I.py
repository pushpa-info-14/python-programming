from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = 0
        min_even = len(s)

        for value in freq.values():
            if value % 2:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)
        return max_odd - min_even


s = Solution()
print(s.maxDifference("aaaaabbc"))
print(s.maxDifference("abcabcab"))
