from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()

        for i in nums1:
            set1.add(i)
        for i in nums2:
            if i in set1:
                set2.add(i)

        return list(set2)


s = Solution()
print(s.intersection([1, 2, 1], [2, 2]))
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
