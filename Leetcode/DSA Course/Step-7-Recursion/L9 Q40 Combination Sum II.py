from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def dfs(i, cur, summation):
            if summation > target:
                return
            if i == n:
                if summation == target:
                    res.append(cur.copy())
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, summation + candidates[i])
            cur.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, summation)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum([2, 5, 2, 1, 2], 5))
print(s.combinationSum([2], 1))
