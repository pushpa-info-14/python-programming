from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        res = nums[0]
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            # Search space is already sorted
            # Then always nums[low] will be the smaller
            if nums[low] <= nums[high]:
                res = min(res, nums[low])
                break

            # Left half is sorted
            if nums[low] <= nums[mid]:
                res = min(res, nums[low])
                low = mid + 1
            else:  # Right half is sorted
                res = min(res, nums[mid])
                high = mid - 1
        return res


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
