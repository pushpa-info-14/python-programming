from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r = 0
        c = 0
        mp = {
            "UP": [-1, 0],
            "DOWN": [1, 0],
            "LEFT": [0, -1],
            "RIGHT": [0, 1]
        }
        for command in commands:
            dr, dc = mp[command]
            r += dr
            c += dc
        return r * n + c


s = Solution()
print(s.finalPositionOfSnake(n=2, commands=["RIGHT", "DOWN"]))
print(s.finalPositionOfSnake(n=3, commands=["DOWN", "RIGHT", "UP"]))
