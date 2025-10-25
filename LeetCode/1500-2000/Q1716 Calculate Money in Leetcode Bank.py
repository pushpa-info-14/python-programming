class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        total = 0
        if weeks:
            total = 28 * weeks + 7 * (weeks - 1) * weeks // 2

        for i in range(7 * weeks + 1, n + 1):
            total += i // 7 + i % 7
        return total


s = Solution()
print(s.totalMoney(4))
print(s.totalMoney(10))
print(s.totalMoney(20))
print(s.totalMoney(26))
