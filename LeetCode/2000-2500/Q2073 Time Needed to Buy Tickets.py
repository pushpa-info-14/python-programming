from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i in range(len(tickets)):
            q.append([i, tickets[i]])
        t = 0
        while q:
            index, num = q.popleft()
            t += 1
            num -= 1
            if num == 0 and index == k:
                return t
            if num > 0:
                q.append([index, num])
        return 0

    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        t = 0
        for i in range(len(tickets)):
            if i <= k:
                t += min(tickets[k], tickets[i])
            else:
                t += min(tickets[k] - 1, tickets[i])
        return t


s = Solution()
print(s.timeRequiredToBuy(tickets=[2, 3, 2], k=2))
print(s.timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
print("-------------")
print(s.timeRequiredToBuy2(tickets=[2, 3, 2], k=2))
print(s.timeRequiredToBuy2(tickets=[5, 1, 1, 1], k=0))
