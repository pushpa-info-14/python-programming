from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_lookup = set(friends)
        res = []
        for x in order:
            if x in friends_lookup:
                res.append(x)
        return res


s = Solution()
print(s.recoverOrder(order=[3, 1, 2, 5, 4], friends=[1, 3, 4]))
print(s.recoverOrder(order=[1, 4, 5, 3, 2], friends=[2, 5]))
