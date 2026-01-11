from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)  # rows
        n = len(matrix[0])  # columns
        prefix_sum = [[0] * n for _ in range(m)]
        res = 0

        for col in range(n):
            summation = 0
            for row in range(m):
                if matrix[row][col] == "0":
                    summation = 0
                else:
                    summation += 1
                prefix_sum[row][col] = summation

        for row in range(m):
            res = max(res, self.largestRectangleArea(prefix_sum[row]))

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
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


# LeetCode 85
s = Solution()
print(s.maximalRectangle(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                 ["1", "0", "0", "1", "0"]]))
print(s.maximalRectangle(matrix=[["0"]]))
print(s.maximalRectangle(matrix=[["1"]]))
