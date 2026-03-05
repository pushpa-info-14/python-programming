from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stack = []

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num == 0:
                continue
            if not stack or stack[-1] < num:
                res += 1
                stack.append(num)
        return res


s = Solution()
print(s.minOperations(nums=[0, 2]))
print(s.minOperations(nums=[3, 1, 2, 1]))
print(s.minOperations(nums=[1, 2, 1, 2, 1, 2]))
