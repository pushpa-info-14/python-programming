from collections import Counter
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        res = [[], []]
        for num in freq1.keys():
            if num not in freq2:
                res[0].append(num)
        for num in freq2.keys():
            if num not in freq1:
                res[1].append(num)
        return res


s = Solution()
print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(s.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
