from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            publications = n - mid
            if citations[mid] >= publications:
                r = mid - 1
                res = publications
            else:
                l = mid + 1
        return res


s = Solution()
print(s.hIndex([0, 1, 3, 5, 6]))
print(s.hIndex([0, 2, 100]))
print(s.hIndex([100]))
print(s.hIndex([11, 15]))
print(s.hIndex([0]))
print(s.hIndex([0, 1]))
