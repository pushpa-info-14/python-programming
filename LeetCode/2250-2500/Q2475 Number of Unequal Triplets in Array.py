from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        res += 1
        return res

    def unequalTriplets2(self, nums: List[int]) -> int:
        counts = list(Counter(nums).values())
        l = 0
        r = sum(counts)
        res = 0
        for count in counts:
            r -= count
            res += l * count * r
            l += count
        return res


s = Solution()
print(s.unequalTriplets(nums=[4, 4, 2, 4, 3]))
print(s.unequalTriplets(nums=[1, 1, 1, 1, 1]))
print("--------------------")
print(s.unequalTriplets2(nums=[4, 4, 2, 4, 3]))
print(s.unequalTriplets2(nums=[1, 1, 1, 1, 1]))
