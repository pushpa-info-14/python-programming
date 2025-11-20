from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for x in operations:
            if x == '+':
                scores.append(scores[-1] + scores[-2])
            elif x == 'D':
                scores.append(scores[-1] * 2)
            elif x == 'C':
                scores.pop()
            else:
                scores.append(int(x))
        return sum(scores)


s = Solution()
print(s.calPoints(operations=["5", "2", "C", "D", "+"]))
print(s.calPoints(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(s.calPoints(operations=["1", "C"]))
