from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        arr = []
        for i in range(0, n, 2):
            arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr


s = Solution()
print(s.numberGame(nums=[5, 4, 2, 3]))
print(s.numberGame(nums=[2, 5]))
