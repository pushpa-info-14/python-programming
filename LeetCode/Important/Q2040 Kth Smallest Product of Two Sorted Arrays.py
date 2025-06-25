import bisect
from math import ceil
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n2 = len(nums2)

        def get_smaller_product(target):
            smaller = 0

            for x in nums1:
                if x < 0: # lower bound reversed
                    smaller += n2 - bisect.bisect_left(nums2, -(-target // x))
                elif x == 0:
                    if target >= 0:
                        smaller += n2
                else: # upper bound
                    smaller += bisect.bisect_right(nums2, target // x)
            return smaller

        left, right = -10 ** 10, 10 ** 10
        while left <= right:
            mid = (left + right) // 2
            if get_smaller_product(mid) >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left


s = Solution()
print(s.kthSmallestProduct(nums1=[2, 5], nums2=[3, 4], k=2))
print(s.kthSmallestProduct(nums1=[-4, -2, 0, 3], nums2=[2, 4], k=6))
print(s.kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3))
