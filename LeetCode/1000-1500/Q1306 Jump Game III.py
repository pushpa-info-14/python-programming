from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            i1, i2 = i + arr[i], i - arr[i]
            if i1 < n and not visited[i1]:
                q.append(i1)
                visited[i] = True
            if i2 >= 0 and not visited[i2]:
                q.append(i2)
                visited[i2] = True
        return False


s = Solution()
print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(s.canReach(arr=[3, 0, 2, 1, 2], start=2))
