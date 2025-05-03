from collections import deque
from typing import List


class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0

        mod = 10 ** 5
        int_max = 10**9
        distance = [int_max] * mod
        q = deque()
        q.append((0, start))

        while q:
            steps, value = q.popleft()
            for num in arr:
                new_value = (value * num) % mod
                if new_value == end:
                    return steps + 1
                if distance[new_value] > steps + 1:
                    q.append((steps + 1, new_value))
                    distance[new_value] = steps + 1
        return -1


s = Solution()
print(s.minimumMultiplications([2, 5, 7], 3, 30))
print(s.minimumMultiplications([3, 4, 65], 7, 66175))
print(s.minimumMultiplications([20, 14, 1,4, 20], 8, 4288))
