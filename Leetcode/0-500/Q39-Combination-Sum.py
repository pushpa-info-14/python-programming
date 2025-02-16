from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        cur = []

        def backtrack(i, target):
            if target == 0:
                res.append(cur.copy())
                return True
            elif target < 0:
                return False

            for j in range(i, n):
                candidate = candidates[j]
                cur.append(candidate)
                backtrack(j, target - candidate)
                cur.pop()

        backtrack(0, target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        cur = []

        def backtrack(i, target):
            if target == 0:
                res.append(cur.copy())
                return
            elif i == n or target < 0:
                return

            candidate = candidates[i]
            cur.append(candidate)
            backtrack(i, target - candidate)
            cur.pop()

            backtrack(i + 1, target)

        backtrack(0, target)
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum2([2, 3, 6, 7], 7))
print(s.combinationSum2([2, 3, 5], 8))
print(s.combinationSum2([2], 1))
