from collections import Counter
from typing import List


def gcd(a, b):
    while a and b:
        a, b = b, a % b
    return a


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        groups = list(set(counter.values()))
        res = groups[0]
        for x in groups[1:]:
            res = gcd(res, x)
        return res > 1


s = Solution()
print(s.hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1]))
print(s.hasGroupsSizeX(deck=[1, 1, 1, 2, 2, 2, 3, 3]))
