from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Update 0 and negative values to outbound value
        # n + 1 is minimum outbound value
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # print(nums)

        # Mark all the relevant element indexes with negative sign if they exist
        for i in range(n):
            num = abs(nums[i])
            if 0 <= num - 1 < n and nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
        # print(nums)

        # All the elements should be negative if the relevant value exists in the array
        # If the value is positive, relevant value is missing.
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
print(s.firstMissingPositive([1]))
print(s.firstMissingPositive([1, 2, 3, 4, 5]))
print(s.firstMissingPositive([2, 3, 4, 5]))
print(s.firstMissingPositive([0, 2, 2, 1, 1]))
