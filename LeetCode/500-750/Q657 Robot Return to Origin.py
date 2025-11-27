from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {
            'R': [-1, 0],
            'L': [1, 0],
            'U': [0, 1],
            'D': [0, -1]
        }
        x, y = 0, 0
        for key, value in Counter(moves).items():
            dx, dy = directions[key]
            x += dx * value
            y += dy * value
        return x == 0 and y == 0


s = Solution()
print(s.judgeCircle(moves="UD"))
print(s.judgeCircle(moves="LL"))
