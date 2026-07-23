from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        i, j = 0, 0
        while i < n1 and j < n2:
            while j + 1 < n2 and nums1[i] <= nums2[j + 1]:
                j += 1
            res = max(res, j - i)
            i += 1
        return res


s = Solution()
print(s.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
print(s.maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]))
print(s.maxDistance(nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]))
