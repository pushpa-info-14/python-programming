from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        return n if n < 3 else pow(2, n.bit_length())


s = Solution()
print(s.uniqueXorTriplets(nums=[1, 2]))
print(s.uniqueXorTriplets(nums=[3, 1, 2]))
