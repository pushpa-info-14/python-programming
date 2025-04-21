from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_x = 0
        min_x = 0
        x = 0
        for difference in differences:
            x += difference
            max_x = max(max_x, x)
            min_x = min(min_x, x)

        res = upper - lower - (max_x - min_x)
        return res + 1 if res >= 0 else 0


s = Solution()
print(s.numberOfArrays(differences=[1, -3, 4], lower=1, upper=6))
print(s.numberOfArrays(differences=[3, -4, 5, 1, -2], lower=-4, upper=5))
print(s.numberOfArrays(differences=[4, -7, 2], lower=3, upper=6))
