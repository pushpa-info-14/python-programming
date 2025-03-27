from typing import List


class Solution:
    def find_previous_smaller_element(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res

    def find_next_smaller_element(self, nums):
        n = len(nums)
        res = [n] * n
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.find_next_smaller_element(heights)
        pse = self.find_previous_smaller_element(heights)
        res = 0
        for i in range(n):
            res = max(res, heights[i] * (nse[i] - pse[i] - 1))
        return res

    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                element = heights[stack.pop()]
                nse = i
                pse = -1 if not stack else stack[-1]
                res = max(res, element * (nse - pse - 1))
            stack.append(i)
        while stack:
            element = heights[stack.pop()]
            nse = n
            pse = -1 if not stack else stack[-1]
            res = max(res, element * (nse - pse - 1))

        return res


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2, 4]))
print(s.largestRectangleArea2([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea2([2, 4]))
