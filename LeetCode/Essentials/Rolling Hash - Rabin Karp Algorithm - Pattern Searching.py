from typing import List


class Solution:
    def findPattern(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        base = 1315423911
        mod = 10 ** 9 + 7
        size = len(pattern)
        highest_pow = pow(base, size - 1, mod)

        pattern_hash = 0
        for num in pattern:
            pattern_hash = (pattern_hash * base + num) % mod

        current_hash = 0
        l = 0
        for r in range(n):
            current_hash = (current_hash * base + nums[r]) % mod
            if r - l + 1 == size:
                if current_hash == pattern_hash:
                    return True
                current_hash = (current_hash - nums[l] * highest_pow) % mod
                l += 1
        return False


s = Solution()
print(s.findPattern(nums=[3, 3, 3], pattern=[3]))
print(s.findPattern(nums=[2, 1, 2, 3, 3], pattern=[3, 3]))
print(s.findPattern(nums=[1, 1, 2, 2, 1], pattern=[2, 1]))
print(s.findPattern(nums=[1, 1, 2, 2, 1], pattern=[2, 1, 3]))
