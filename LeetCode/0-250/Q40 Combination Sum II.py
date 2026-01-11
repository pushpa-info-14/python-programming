from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        cur = []

        def backtrack(i, target):
            if target == 0:
                res.append(cur.copy())
                return
            elif i == n or target < 0:
                return

            # Include candidates[i]
            candidate = candidates[i]
            cur.append(candidate)
            backtrack(i + 1, target - candidate)
            cur.pop()

            # Skip candidates[i]
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, target)

        backtrack(0, target)
        return res


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
