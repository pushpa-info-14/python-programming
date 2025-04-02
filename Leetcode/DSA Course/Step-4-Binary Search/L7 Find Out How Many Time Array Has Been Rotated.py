from typing import List


class Solution:
    def howMany(self, nums: List[int]) -> int:
        n = len(nums)

        minimum = nums[0]
        index = 0
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            # Search space is already sorted
            # Then always nums[low] will be the smaller
            if nums[low] <= nums[high]:
                if nums[low] < minimum:
                    minimum = nums[low]
                    index = low
                break

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] < minimum:
                    minimum = nums[low]
                    index = low
                low = mid + 1
            else:  # Right half is sorted
                if nums[mid] < minimum:
                    minimum = nums[mid]
                    index = mid
                high = mid - 1
        return index


s = Solution()
print(s.howMany([3, 4, 5, 1, 2]))
print(s.howMany([4, 5, 6, 7, 0, 1, 2]))
print(s.howMany([11, 13, 15, 17]))
