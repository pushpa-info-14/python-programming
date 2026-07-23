from math import inf
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = set()
        last = nums[0] - k
        for num in nums:
            last = max(last, num - k)
            for new_num in range(last, num + k + 1):
                if new_num not in seen:
                    seen.add(new_num)
                    last = new_num
                    break
        return len(seen)

    def maxDistinctElements2(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        next_available = -inf
        for num in nums:
            if num - k >= next_available:
                next_available = num - k + 1
                res += 1
                continue
            if num - k < next_available <= num + k:
                next_available += 1
                res += 1
        return res


s = Solution()
print(s.maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2))
print(s.maxDistinctElements(nums=[4, 4, 4, 4], k=1))
print(s.maxDistinctElements(nums=[56, 56, 54, 54], k=0))
print(s.maxDistinctElements2(nums=[1, 2, 2, 3, 3, 4], k=2))
print(s.maxDistinctElements2(nums=[4, 4, 4, 4], k=1))
print(s.maxDistinctElements2(nums=[56, 56, 54, 54], k=0))
