from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        maxi = -1

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                maxi = max(maxi, nums[i] - nums[stack[0]])
            stack.append(i)
        return maxi


s = Solution()
print(s.maximumDifference(nums=[7, 1, 5, 4]))
print(s.maximumDifference(nums=[9, 4, 3, 2]))
print(s.maximumDifference(nums=[1, 5, 2, 10]))
