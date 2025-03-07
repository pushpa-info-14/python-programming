from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, cur):
            res.append(cur.copy())

            for j in range(i, n):
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()

        dfs(0, [])
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([0]))

print(s.subsets2([1, 2, 3]))
print(s.subsets2([0]))
