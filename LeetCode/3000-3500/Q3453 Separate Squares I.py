from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(target):
            top, bottom = 0, 0
            for x, y, l in squares:
                if y + l <= target:
                    bottom += l * l
                elif y > target:
                    top += l * l
                else:
                    top += (y + l - target) * l
                    bottom += (target - y) * l
            return bottom >= top

        accuracy = 10 ** -5
        low, high = 0, 10 ** 9
        while abs(low - high) > accuracy:
            mid = (low + high) / 2
            if check(mid):
                high = mid
            else:
                low = mid
        return low


s = Solution()
print(s.separateSquares(squares=[[0, 0, 1], [2, 2, 1]]))
print(s.separateSquares(squares=[[0, 0, 2], [1, 1, 1]]))
print(s.separateSquares(squares=[[23, 29, 3], [28, 29, 4]]))
