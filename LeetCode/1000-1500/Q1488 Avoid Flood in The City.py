from bisect import bisect_right
from typing import List

from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = SortedList()
        full = {}
        out = []
        for d, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(d)
                out.append(1)
                continue
            out.append(-1)
            if lake not in full:
                full[lake] = d
                continue
            i = bisect_right(dry_days, full[lake])
            if i == len(dry_days):
                return []
            out[dry_days[i]] = lake
            full[lake] = d
            dry_days.remove(dry_days[i])
        return out


s = Solution()
print(s.avoidFlood(rains=[1, 2, 3, 4]))
print(s.avoidFlood(rains=[1, 2, 0, 0, 2, 1]))
print(s.avoidFlood(rains=[1, 2, 0, 1, 2]))
print(s.avoidFlood(rains=[69, 0, 0, 0, 69]))
