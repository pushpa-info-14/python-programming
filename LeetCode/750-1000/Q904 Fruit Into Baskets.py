from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l, r = 0, 0
        max_fruits = 0
        types = defaultdict(int)
        while r < n:
            types[fruits[r]] += 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1

            max_fruits = max(max_fruits, r - l + 1)
            r += 1

        return max_fruits


# Max length of subarray with at most 2 unique numbers
s = Solution()
print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 2, 2]))
