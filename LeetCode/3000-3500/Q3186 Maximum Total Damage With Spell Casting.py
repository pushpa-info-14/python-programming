from collections import Counter
from functools import cache
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq.keys())
        n = len(keys)

        @cache
        def get_max(index):
            if index >= n:
                return 0
            # no take
            best = get_max(index + 1)
            # take
            next_index = index + 1
            while next_index < n and keys[next_index] <= keys[index] + 2:
                next_index += 1
            best = max(best, get_max(next_index) + keys[index] * freq[keys[index]])
            return best

        return get_max(0)


s = Solution()
print(s.maximumTotalDamage(power=[1, 1, 3, 4]))
print(s.maximumTotalDamage(power=[7, 1, 6, 6]))
print(s.maximumTotalDamage(power=[5, 9, 2, 10, 2, 7, 10, 9, 3, 8]))
