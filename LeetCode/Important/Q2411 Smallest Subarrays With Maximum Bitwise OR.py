import math
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_val = max(nums)
        bits = 0 if max_val == 0 else 1 + math.floor(math.log2(max_val))

        # Track next greater element (NGE)
        nearest_set_bit = [n] * bits
        res = [0] * n
        for i in reversed(range(n)):
            nearest = i
            for j in range(bits):
                if nums[i] & (1 << j):
                    nearest_set_bit[j] = i
                elif nearest_set_bit[j] != n:
                    nearest = max(nearest, nearest_set_bit[j])
            res[i] = nearest - i + 1
        return res


s = Solution()
print(s.smallestSubarrays(nums=[1, 0, 2, 1, 3]))
print(s.smallestSubarrays(nums=[1, 2]))
