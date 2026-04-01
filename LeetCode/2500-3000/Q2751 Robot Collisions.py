from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        events = []
        for i in range(n):
            events.append((positions[i], i))
        events.sort()

        stack = []
        for _, i in events:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[stack[-1]] <= healths[i]:
                    removed = stack.pop()
                    if healths[removed] == healths[i]:
                        healths[i] = 0
                    else:
                        healths[i] -= 1
                    healths[removed] = 0
                if stack and healths[i]:
                    healths[stack[-1]] -= 1
                    healths[i] = 0

        return [x for x in healths if x > 0]


s = Solution()
print(s.survivedRobotsHealths(positions=[5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR"))
print(s.survivedRobotsHealths(positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))
print(s.survivedRobotsHealths(positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"))
