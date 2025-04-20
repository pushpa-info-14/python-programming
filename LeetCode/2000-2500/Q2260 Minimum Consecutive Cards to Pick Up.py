import math
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        res = math.inf
        mp = {}

        for i, num in enumerate(cards):
            if num in mp:
                res = min(res, i - mp[num] + 1)
            mp[num] = i

        return res if res != math.inf else -1

    def minimumCardPickup2(self, cards: List[int]) -> int:
        n = len(cards)
        freq = {}
        res = math.inf

        l, r = 0, 0
        while r < n:
            if cards[r] not in freq:
                freq[cards[r]] = 0
            freq[cards[r]] += 1

            while l < r and freq[cards[r]] == 2:
                res = min(res, r - l + 1)
                freq[cards[l]] -= 1
                if freq[cards[l]] == 0:
                    del freq[cards[l]]
                l += 1
            r += 1
        return res if res != math.inf else -1


s = Solution()
print(s.minimumCardPickup([3, 4, 2, 3, 4, 7]))
print(s.minimumCardPickup2([3, 4, 2, 3, 4, 7]))
print(s.minimumCardPickup([1, 0, 5, 3]))
print(s.minimumCardPickup2([1, 0, 5, 3]))
