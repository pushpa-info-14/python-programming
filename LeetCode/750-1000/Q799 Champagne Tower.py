class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * i for i in range(1, query_row + 3)]
        dp[0][0] = poured
        for row in range(1, query_row + 2):
            for glass in range(1, row + 1):
                if dp[row - 1][glass - 1] > 1:
                    cur = (dp[row - 1][glass - 1] - 1) / 2.0
                    dp[row][glass - 1] += cur
                    dp[row][glass] += cur
                    dp[row - 1][glass - 1] = 1
        return dp[query_row][query_glass]

    def champagneTower2(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for _ in range(query_row):
            cur = [0] * (len(row) + 1)
            for i in range(len(row)):
                if row[i] > 1:
                    v = (row[i] - 1) / 2.0
                    cur[i] += v
                    cur[i + 1] += v
            row = cur
        return row[query_glass] if row[query_glass] < 1 else 1.0


s = Solution()
print(s.champagneTower(poured=1, query_row=1, query_glass=1))
print(s.champagneTower(poured=2, query_row=1, query_glass=1))
print(s.champagneTower(poured=100000009, query_row=33, query_glass=17))
print(s.champagneTower(poured=1000000000, query_row=99, query_glass=99))
print("---------------")
print(s.champagneTower2(poured=1, query_row=1, query_glass=1))
print(s.champagneTower2(poured=2, query_row=1, query_glass=1))
print(s.champagneTower2(poured=100000009, query_row=33, query_glass=17))
print(s.champagneTower2(poured=1000000000, query_row=99, query_glass=99))
