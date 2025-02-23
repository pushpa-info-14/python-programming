from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        i = 0
        for num in less:
            nums[i] = num
            i += 1
        for num in equal:
            nums[i] = num
            i += 1
        for num in greater:
            nums[i] = num
            i += 1

        return nums


s = Solution()
print(s.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
print(s.pivotArray([-3, 4, 3, 2], 2))
