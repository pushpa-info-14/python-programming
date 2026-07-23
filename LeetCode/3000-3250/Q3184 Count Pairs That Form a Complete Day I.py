from collections import defaultdict
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        counter = defaultdict(int)
        for x in hours:
            x %= 24
            target = x
            if target != 0:
                target = 24 - target
            if target in counter:
                res += counter[target]
            counter[x] += 1
        return res


s = Solution()
print(s.countCompleteDayPairs(hours=[12, 12, 30, 24, 24]))
print(s.countCompleteDayPairs(hours=[72, 48, 24, 3]))
