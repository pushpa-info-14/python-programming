from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        res = []
        for i in range(1, n - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                res.append(i)
        return res


s = Solution()
print(s.findPeaks(mountain=[2, 4, 4]))
print(s.findPeaks(mountain=[1, 4, 3, 8, 5]))
