from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0] * 3
        for val in stones:
            count[val % 3] += 1

        if count[0] & 1 == 0:
            return count[1] >= 1 and count[2] >= 1
        return abs(count[1] - count[2]) > 2


s = Solution()
print(s.stoneGameIX(stones=[2, 1]))
print(s.stoneGameIX(stones=[2]))
print(s.stoneGameIX(stones=[5, 1, 2, 4, 3]))
