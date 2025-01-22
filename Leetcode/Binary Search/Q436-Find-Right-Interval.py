from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_map = {interval[0]: i for i, interval in enumerate(intervals)}
        start_sorted = sorted([interval[0] for interval in intervals])
        res = []
        for start, end in intervals:
            target = end
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if target > start_sorted[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == n:
                res.append(-1)
            else:
                res.append(start_map[start_sorted[l]])
        return res


s = Solution()
print(s.findRightInterval([[1, 2]]))
print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))
print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))
print(s.findRightInterval([[4, 4]]))
