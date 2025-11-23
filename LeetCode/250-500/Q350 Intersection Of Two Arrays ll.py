from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seenDict = {}
        result = []

        for i in nums1:
            if i in seenDict:
                seenDict[i] += 1
            else:
                seenDict[i] = 1
        for i in nums2:
            if seenDict.get(i, 0) > 0:
                result.append(i)
                seenDict[i] -= 1
        return result


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
