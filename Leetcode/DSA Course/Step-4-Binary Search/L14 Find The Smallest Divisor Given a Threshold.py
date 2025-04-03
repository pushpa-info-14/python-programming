import math
from typing import List


def findThreshold(nums, divisor):
    count = 0
    for num in nums:
        count += int(math.ceil(num / divisor))
    return count


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n > threshold: return -1

        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2

            if findThreshold(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.smallestDivisor([1, 2, 5, 9], 6))
print(s.smallestDivisor([44, 22, 33, 11, 1], 5))
