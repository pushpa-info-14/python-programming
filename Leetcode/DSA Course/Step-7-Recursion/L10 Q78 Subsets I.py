from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, cur, summation):
            if i == n:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1, cur, summation + nums[i])
            cur.pop()
            dfs(i + 1, cur, summation)

        dfs(0, [], 0)
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([0]))
