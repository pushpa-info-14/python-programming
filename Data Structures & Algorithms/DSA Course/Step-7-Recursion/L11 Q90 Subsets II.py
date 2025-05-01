from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)

        dfs(0, [])
        return res

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def dfs(i, cur):
            res.append(cur.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]: continue
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()

        dfs(0, [])
        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([0]))

print(s.subsetsWithDup2([1, 2, 2]))
print(s.subsetsWithDup2([0]))
