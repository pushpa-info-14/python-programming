from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        next_time = 0
        for i in timeSeries:
            if next_time <= i:
                total += duration
            else:
                total = total - (next_time - i) + duration
            next_time = i + duration
        return total


s = Solution()
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 2], 2))
print(s.findPoisonedDuration([1, 2, 3, 4], 2))
print(s.findPoisonedDuration([1, 2, 7], 2))
