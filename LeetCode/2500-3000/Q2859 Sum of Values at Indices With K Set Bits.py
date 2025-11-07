from typing import List


def count_set_bits(num):
    res = 0
    while num:
        res += 1
        num &= num - 1
    return res


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            if count_set_bits(i) == k:
                res += nums[i]
        return res


s = Solution()
print(s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1))
print(s.sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2))
