from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        profit = 0
        q = deque()
        closed = set()
        for node in initialBoxes:
            if status[node]:
                q.append(node)
            else:
                closed.add(node)

        while q:
            node = q.popleft()

            for key in keys[node]:
                status[key] = 1
                if key in closed:
                    q.append(key)
                    closed.remove(key)

            profit += candies[node]
            candies[node] = 0

            for nei in containedBoxes[node]:
                if status[nei]:
                    q.append(nei)
                else:
                    closed.add(nei)

        return profit


s = Solution()
print(s.maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
                   containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]))
print(s.maxCandies(status=[1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1], keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                   containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initialBoxes=[0]))
