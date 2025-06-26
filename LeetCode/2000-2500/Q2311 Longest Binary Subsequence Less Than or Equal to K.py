class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        used_ones = 0
        used_zeros = 0
        power = 1
        number = 0
        for c in s[::-1]:
            if c == '1':
                if number + power <= k:
                    number += power
                    used_ones += 1
            else:
                used_zeros += 1
            power <<= 1

        return used_zeros + used_ones


s = Solution()
print(s.longestSubsequence(s="1001010", k=5))
print(s.longestSubsequence(s="00101001", k=1))
