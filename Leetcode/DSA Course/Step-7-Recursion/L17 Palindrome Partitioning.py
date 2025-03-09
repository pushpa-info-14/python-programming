from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            for j in range(i, n):
                if isPalindrome(i, j):
                    cur.append(s[i:j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res


s = Solution()
print(s.partition("aabb"))
