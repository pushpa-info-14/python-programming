from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            asteroid = asteroids[i]
            while stack and stack[-1] > 0 > asteroid:
                if stack[-1] > abs(asteroid):
                    asteroid = 0
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)
        return stack

    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            asteroid = asteroids[i]
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
        return stack


s = Solution()
print(s.asteroidCollision(asteroids=[4, 7, 1, 1, 2, -3, -7, 17, 15, -16]))
print(s.asteroidCollision(asteroids=[5, 10, -5]))
print(s.asteroidCollision(asteroids=[8, -8]))
print(s.asteroidCollision(asteroids=[8, -9]))
print(s.asteroidCollision(asteroids=[10, 2, -5]))

print(s.asteroidCollision2(asteroids=[4, 7, 1, 1, 2, -3, -7, 17, 15, -16]))
print(s.asteroidCollision2(asteroids=[5, 10, -5]))
print(s.asteroidCollision2(asteroids=[8, -8]))
print(s.asteroidCollision2(asteroids=[8, -9]))
print(s.asteroidCollision2(asteroids=[10, 2, -5]))
