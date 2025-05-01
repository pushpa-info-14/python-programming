from typing import List


class Solution:
    def sumOfSubsets(self, weights: List[int], target: int) -> List[List[int]]:
        n = len(weights)
        res = []

        def backtracking(level, cur_sum, cur_res):
            if cur_sum == target:
                res.append(cur_res.copy())
                return True
            if cur_sum > target:
                return False
            if level == n - 1:
                return False

            s1 = backtracking(level + 1, cur_sum, cur_res)

            cur_res.append(weights[level + 1])
            s2 = backtracking(level + 1, cur_sum + weights[level + 1], cur_res)
            cur_res.remove(weights[level + 1])

            return s1 or s2

        backtracking(0, 0, [])
        backtracking(0, weights[0], [weights[0]])
        return res


s = Solution()
print(s.sumOfSubsets([5, 10, 12, 13, 15, 18], 30))
