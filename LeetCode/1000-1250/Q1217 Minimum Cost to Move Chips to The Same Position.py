from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        parity_odd = 0
        parity_even = 0
        for pos in position:
            if pos & 1:
                parity_odd += 1
            else:
                parity_even += 1
        return min(parity_odd, parity_even)


s = Solution()
print(s.minCostToMoveChips(position=[1, 2, 3]))
print(s.minCostToMoveChips(position=[2, 2, 2, 3, 3]))
print(s.minCostToMoveChips(position=[1, 1000000000]))
