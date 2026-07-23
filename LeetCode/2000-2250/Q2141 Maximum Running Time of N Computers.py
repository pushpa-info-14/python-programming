from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(target):
            max_minutes = 0
            for x in batteries:
                max_minutes += min(target, x)
            return max_minutes >= n * target

        low, high = 0, sum(batteries) // n
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high


s = Solution()
print(s.maxRunTime(n=2, batteries=[3, 3, 3]))  # 4
print(s.maxRunTime(n=2, batteries=[1, 1, 1, 1]))  # 2
print(s.maxRunTime(n=3, batteries=[10, 10, 6, 9, 3]))  # 12
print(s.maxRunTime(n=3, batteries=[10, 10, 3, 5]))  # 8
