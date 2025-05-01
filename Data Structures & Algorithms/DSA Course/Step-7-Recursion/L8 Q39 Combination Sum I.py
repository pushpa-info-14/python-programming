from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        def dfs(i, cur, summation):
            if summation > target:
                return
            if i == n:
                if summation == target:
                    res.append(cur.copy())
                return
            cur.append(candidates[i])
            dfs(i, cur, summation + candidates[i])
            cur.pop()
            dfs(i + 1, cur, summation)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
