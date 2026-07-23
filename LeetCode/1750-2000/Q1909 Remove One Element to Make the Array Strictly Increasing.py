from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            flag = True
            arr = nums[:i] + nums[i + 1:]
            for j in range(1, len(arr)):
                if arr[j - 1] >= arr[j]:
                    flag = False
                    break
            if flag:
                return True
        return False


s = Solution()
print(s.canBeIncreasing(nums=[1, 2, 10, 5, 7]))
print(s.canBeIncreasing(nums=[2, 3, 1, 2]))
print(s.canBeIncreasing(nums=[1, 1, 1]))
print(s.canBeIncreasing(nums=[100, 21, 3]))
