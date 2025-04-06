import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        low, high = 0, n1
        left = (n1 + n2 + 1) // 2
        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = left - mid1
            l1, l2 = -math.inf, -math.inf
            r1, r2 = math.inf, math.inf
            if mid1 < n1: r1 = nums1[mid1]
            if mid2 < n2: r2 = nums2[mid2]
            if mid1 - 1 >= 0: l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0: l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if n % 2:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3, 4, 7, 10, 12], nums2=[2, 3, 6, 15]))
print(s.findMedianSortedArrays(nums1=[2, 3, 4], nums2=[1, 3]))
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
print(s.findMedianSortedArrays(nums1=[1, 2, 3], nums2=[]))
