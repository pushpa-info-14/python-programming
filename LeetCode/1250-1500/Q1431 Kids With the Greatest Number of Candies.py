from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        res = []
        for x in candies:
            if x + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(s.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(s.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
