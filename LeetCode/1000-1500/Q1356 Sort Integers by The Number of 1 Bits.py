from collections import defaultdict
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        mp = defaultdict(list)

        for num in arr:
            x = num
            bits = 0
            while x:
                bits += 1
                x &= x - 1
            mp[bits].append(num)

        res = []
        for key in sorted(mp.keys()):
            res += mp[key]
        return res


s = Solution()
print(s.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(s.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
