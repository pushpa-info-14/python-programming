from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob = set()
        for x, y in obstacles:
            ob.add((x, y))
        res = 0
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = directions[d]
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in ob:
                        break
                    x = nx
                    y = ny
                    res = max(res, x * x + y * y)
        return res


s = Solution()
print(s.robotSim(commands=[4, -1, 3], obstacles=[]))
print(s.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))
print(s.robotSim(commands=[6, -1, -1, 6], obstacles=[[0, 0]]))
