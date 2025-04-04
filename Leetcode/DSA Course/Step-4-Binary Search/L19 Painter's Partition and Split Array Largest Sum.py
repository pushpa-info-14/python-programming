from typing import List


def numOfPainters(nums, max_time):
    painters = 1
    time_taken = 0
    for num in nums:
        if time_taken + num <= max_time:
            time_taken += num
        else:
            painters += 1
            time_taken = num
    return painters


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if numOfPainters(nums, mid) <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.splitArray(nums=[7, 2, 5, 10, 8], k=2))
print(s.splitArray(nums=[1, 2, 3, 4, 5], k=2))
