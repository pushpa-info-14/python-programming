import math
from typing import List


def kthElement(nums1: List[int], nums2: List[int], k):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return kthElement(nums2, nums1, k)
    low, high = max(0, k - n2), min(n1, k)
    left = k
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
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 4))
print(kthElement([2, 4, 5], [1, 3], 3))
