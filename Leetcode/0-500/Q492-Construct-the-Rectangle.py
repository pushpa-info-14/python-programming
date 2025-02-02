import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        min_value = math.inf
        res = [area, 1]  # l, w

        for w in range(2, int(area ** 0.5) + 1):
            if area % w == 0:
                l = area // w
                if l - w < min_value:
                    res[0] = l
                    res[1] = w
                    min_value = l - w

        return res


s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(37))
