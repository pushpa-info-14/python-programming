from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        n1, n2 = len(nums1), len(nums2)
        l1, l2 = 0, 0

        while l1 < n1 and l2 < n2:
            if nums1[l1][0] < nums2[l2][0]:
                res.append(nums1[l1])
                l1 += 1
            elif nums1[l1][0] > nums2[l2][0]:
                res.append(nums2[l2])
                l2 += 1
            else:
                res.append([nums1[l1][0], nums1[l1][1] + nums2[l2][1]])
                l1 += 1
                l2 += 1
        while l1 < n1:
            res.append(nums1[l1])
            l1 += 1
        while l2 < n2:
            res.append(nums2[l2])
            l2 += 1

        return res


s = Solution()
print(s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
print(s.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
