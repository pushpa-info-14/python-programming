from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[1], -i[0]))
        p1, p2 = -1, -1
        res = 0
        for left, right in intervals:
            if p2 < left:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                p1, p2 = p2, right
        return res

    def intersectionSizeTwo2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[1], i[0]))
        p1, p2 = -1, -1
        res = 0
        for left, right in intervals:
            if p2 < left:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                if p2 == right:
                    p1 = right - 1
                else:
                    p1, p2 = p2, right
        return res


s = Solution()
print(s.intersectionSizeTwo(intervals=[[1, 3], [3, 7], [8, 9]]))
print(s.intersectionSizeTwo(intervals=[[1, 3], [1, 4], [2, 5], [3, 5]]))
print(s.intersectionSizeTwo(intervals=[[1, 2], [2, 3], [2, 4], [4, 5]]))
print(s.intersectionSizeTwo2(intervals=[[1, 3], [3, 7], [8, 9]]))
print(s.intersectionSizeTwo2(intervals=[[1, 3], [1, 4], [2, 5], [3, 5]]))
print(s.intersectionSizeTwo2(intervals=[[1, 2], [2, 3], [2, 4], [4, 5]]))
