from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        inf = 10 ** 10

        @cache
        def dfs(i, j, is_empty):
            if i >= n1 or j >= n2:
                return -inf if is_empty else 0
            return max(
                nums1[i] * nums2[j] + dfs(i + 1, j + 1, False),
                dfs(i, j + 1, is_empty),
                dfs(i + 1, j, is_empty)
            )

        return dfs(0, 0, True)


s = Solution()
print(s.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
print(s.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))
print(s.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))
