from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        l, r = 0, 0
        max_fruits = 0
        types = {}
        while r < n:
            if fruits[r] not in types:
                types[fruits[r]] = 0
            types[fruits[r]] += 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1

            max_fruits = max(max_fruits, r - l + 1)
            r += 1

        return max_fruits

    def totalFruit2(self, fruits: List[int]) -> int:

        n = len(fruits)
        l, r = 0, 0
        max_fruits = 0
        types = {}
        while r < n:
            if fruits[r] not in types:
                types[fruits[r]] = 0
            types[fruits[r]] += 1

            if len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1
            if len(types) <= 2:
                max_fruits = max(max_fruits, r - l + 1)
            r += 1

        return max_fruits


s = Solution()
print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 2, 2]))

print(s.totalFruit2([1, 2, 1]))
print(s.totalFruit2([0, 1, 2, 2]))
print(s.totalFruit2([1, 2, 3, 2, 2]))
