import bisect
from math import ceil
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n_spell = len(spells)
        n_potions = len(potions)
        res = [0] * n_spell
        potions.sort()
        for idx, spell in enumerate(spells):
            target = ceil(success / spell)
            i = bisect.bisect_left(potions, target)
            res[idx] = n_potions - i
        return res


s = Solution()
print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
