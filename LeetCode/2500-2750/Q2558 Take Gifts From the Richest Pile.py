import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = [-x for x in gifts]
        heapq.heapify(q)
        for _ in range(k):
            x = heapq.heappop(q)
            x = -x
            if x == 1:
                return len(gifts)
            x = int(math.sqrt(x))
            heapq.heappush(q, -x)

        return -sum(q)


s = Solution()
print(s.pickGifts(gifts=[25, 64, 9, 4, 100], k=4))
print(s.pickGifts(gifts=[1, 1, 1, 1], k=4))
