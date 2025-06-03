from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        profit = 0
        q1 = deque()
        q2 = deque()
        for node in initialBoxes:
            if status[node]:
                q1.append(node)
            else:
                q2.append(node)

        while q1:
            node = q1.popleft()

            for key in keys[node]:
                status[key] = 1

            profit += candies[node]
            candies[node] = 0

            for nei in containedBoxes[node]:
                if status[nei]:
                    q1.append(nei)
                else:
                    q2.append(node)

        while q2:
            node = q2.popleft()

            for key in keys[node]:
                status[key] = 1

            if status[node]:
                profit += candies[node]
                candies[node] = 0

                for nei in containedBoxes[node]:
                    if status[nei]:
                        q2.append(nei)

        return profit


s = Solution()
print(s.maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
                   containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]))
print(s.maxCandies(status=[1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1], keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                   containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initialBoxes=[0]))
