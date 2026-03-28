from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        cur = 1
        letters = [0] * n

        for i in range(n):
            if letters[i]:
                continue
            if cur > 26:
                return ""
            for j in range(i, n):
                if lcp[i][j]:
                    letters[j] = cur
            cur += 1

        for i in range(n):
            for j in range(n):
                if letters[i] != letters[j]:
                    expected = 0
                else:
                    expected = (lcp[i + 1][j + 1] if i < n - 1 and j < n - 1 else 0) + 1
                if expected != lcp[i][j]:
                    return ""

        res = ""
        for num in letters:
            res += chr(ord('a') - 1 + num)
        return res


s = Solution()
print(s.findTheString(lcp=[[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]))
print(s.findTheString(lcp=[[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]]))
print(s.findTheString(lcp=[[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]]))
