from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        freq = [False] * n

        def dfs(cur):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if not freq[i]:
                    freq[i] = True
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
                    freq[i] = False
        dfs([])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
