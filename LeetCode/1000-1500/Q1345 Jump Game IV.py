from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = defaultdict(list)
        for i in range(n):
            mp[arr[i]].append(i)
        visited = [False] * n
        q = deque()
        q.append((0, 0))  # steps, index
        visited[0] = True
        while q:
            steps, i = q.popleft()
            if i == n - 1:
                return steps
            if i - 1 >= 0 and not visited[i - 1]:
                q.append((steps + 1, i - 1))
                visited[i - 1] = True
            if i + 1 < n and not visited[i + 1]:
                q.append((steps + 1, i + 1))
                visited[i + 1] = True
            if arr[i] in mp:
                for j in mp[arr[i]]:
                    if i != j and not visited[j]:
                        q.append((steps + 1, j))
                        visited[j] = True
                del mp[arr[i]]
        return 0


s = Solution()
print(s.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
print(s.minJumps(arr=[7]))
print(s.minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]))
