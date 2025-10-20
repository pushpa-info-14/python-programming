from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if '+' in o:
                x += 1
            else:
                x -= 1
        return x


s = Solution()
print(s.finalValueAfterOperations(operations=["--X", "X++", "X++"]))
print(s.finalValueAfterOperations(operations=["++X", "++X", "X++"]))
print(s.finalValueAfterOperations(operations=["X++", "++X", "--X", "X--"]))
