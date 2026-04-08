from typing import List


class Robot:
    map = {0: "East", 1: "North", 2: "West", 3: "South"}
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cur, x, y = 0, 0, 0
    steps = 0

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.mod = (self.width + self.height) * 2 - 4

    def step(self, num: int) -> None:
        self.steps += num

    def _move(self):
        if self.steps == 0:
            return
        num = self.steps %self.mod
        self.steps = 0
        if num == 0:
            if (self.x, self.y) == (0, 0) and self.cur != 3:
                self.cur = (self.cur - 1) % 4
            elif (self.x, self.y) == (self.width - 1, 0) and self.cur != 0:
                self.cur = (self.cur - 1) % 4
            elif (self.x, self.y) == (self.width - 1, self.height - 1) and self.cur != 1:
                self.cur = (self.cur - 1) % 4
            elif (self.x, self.y) == (0, self.height - 1) and self.cur != 2:
                self.cur = (self.cur - 1) % 4
        for _ in range(num):
            dx, dy = self.directions[self.cur]
            nx, ny = self.x + dx, self.y + dy
            if nx < 0 or nx == self.width or ny < 0 or ny == self.height:
                self.cur = (self.cur + 1) % 4
                dx, dy = self.directions[self.cur]
                nx, ny = self.x + dx, self.y + dy
            self.x = nx
            self.y = ny

    def getPos(self) -> List[int]:
        self._move()
        return [self.x, self.y]

    def getDir(self) -> str:
        self._move()
        return self.map[self.cur]


robot = Robot(6, 3)
robot.step(2)
robot.step(2)
print(robot.getPos())
print(robot.getDir())
robot.step(2)
robot.step(1)
robot.step(4)
print(robot.getPos())
print(robot.getDir())
print("-----------")
robot = Robot(97, 98)
print(robot.getPos())
print(robot.getDir())
robot.step(66392)
robot.step(83376)
robot.step(71796)
robot.step(57514)
robot.step(36284)
robot.step(69866)
robot.step(31652)
robot.step(32038)
print(robot.getDir())
print(robot.getPos())
