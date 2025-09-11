from functools import cache
from math import inf
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        for i in range(m):
            languages[i] = set(languages[i])

        @cache
        def f(user1, user2) -> bool:
            return any(languages[user1 - 1] & languages[user2 - 1])

        res = inf
        for l in range(1, n + 1):
            hash_set = set()
            for u, v in friendships:
                if not f(u, v):
                    if l not in languages[u - 1]:
                        hash_set.add(u)
                    if l not in languages[v - 1]:
                        hash_set.add(v)
                    if len(hash_set) >= res:
                        break
            if len(hash_set) < res:
                res = len(hash_set)

        return res

s = Solution()
print(s.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))
print(s.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))