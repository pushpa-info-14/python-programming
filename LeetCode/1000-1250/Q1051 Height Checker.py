from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_copy = heights.copy()
        heights_copy.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights_copy[i]:
                res += 1
        return res


s = Solution()
print(s.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
print(s.heightChecker(heights=[5, 1, 2, 3, 4]))
print(s.heightChecker(heights=[1, 2, 3, 4, 5]))
