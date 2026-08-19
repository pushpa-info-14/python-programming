from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        res = n * 2
        row = 1
        i = 0
        while i < len(reservedSeats):
            values = [0] * 11
            while i < len(reservedSeats) and reservedSeats[i][0] == row:
                values[reservedSeats[i][1]] = 1
                i += 1
            cur = 0
            l = 2
            for r in range(2, 10):
                if values[r] == 1:
                    l = r + 1
                if r in [5, 7, 9] and r - l + 1 >= 4:
                    cur += 1
                    l = r + 1
            res -= (2 - cur)
            row += 1
        return res

    def maxNumberOfFamilies2(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        res = (n - len(occupied)) * 2
        for row, bitmask in occupied.items():
            if (bitmask | left) == left or (bitmask | middle) == middle or (bitmask | right) == right:
                res += 1
        return res


s = Solution()
print(s.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(s.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(s.maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
print("---------------------")
print(s.maxNumberOfFamilies2(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(s.maxNumberOfFamilies2(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(s.maxNumberOfFamilies2(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
