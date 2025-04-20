class Solution:
    def totalNQueens(self, n: int) -> int:
        pos_diagonal = set()
        neg_diagonal = set()
        column = set()

        def dfs(r):
            if r == n:
                return 1

            cnt = 0
            for c in range(n):
                if c in column or r + c in pos_diagonal or r - c in neg_diagonal:
                    continue
                column.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)
                cnt += dfs(r + 1)
                column.remove(c)
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)
            return cnt

        return dfs(0)


s = Solution()
print(s.totalNQueens(4))
print(s.totalNQueens(1))
