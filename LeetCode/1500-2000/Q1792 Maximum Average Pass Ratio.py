import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for s_pass, s_total in classes:
            increment = ((s_pass + 1) / (s_total + 1)) - (s_pass / s_total)
            heapq.heappush(q, (-increment, s_pass, s_total))

        for i in range(extraStudents):
            _, s_pass, s_total = heapq.heappop(q)
            s_pass += 1
            s_total += 1
            increment = ((s_pass + 1) / (s_total + 1)) - (s_pass / s_total)
            heapq.heappush(q, (-increment, s_pass, s_total))

        total_ratio = 0
        while q:
            _, s_pass, s_total = heapq.heappop(q)
            total_ratio += s_pass / s_total

        return total_ratio / len(classes)

    def maxAverageRatio2(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        q = []
        for i in range(n):
            increment = ((classes[i][0] + 1) / (classes[i][1] + 1)) - (classes[i][0] / classes[i][1])
            heapq.heappush(q, (-increment, i))

        for _ in range(extraStudents):
            _, i = heapq.heappop(q)
            classes[i][0] += 1
            classes[i][1] += 1
            increment = ((classes[i][0] + 1) / (classes[i][1] + 1)) - (classes[i][0] / classes[i][1])
            heapq.heappush(q, (-increment, i))

        total_ratio = 0
        while q:
            _, i = heapq.heappop(q)
            total_ratio += classes[i][0] / classes[i][1]

        return total_ratio / len(classes)


s = Solution()
print(s.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
print(s.maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4))
print(s.maxAverageRatio2(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
print(s.maxAverageRatio2(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4))
