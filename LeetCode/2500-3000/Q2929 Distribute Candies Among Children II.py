def cal(x):
    if x < 0:
        return 0
    return x * (x - 1) // 2

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
        return ans

    def distributeCandies2(self, n: int, limit: int) -> int:
        return (
            cal(n + 2)
            - 3 * cal(n - limit + 1)
            + 3 * cal(n - (limit + 1) * 2 + 2)
            - cal(n - 3 * (limit + 1) + 2)
        )

s = Solution()
print(s.distributeCandies(5, 2))
print(s.distributeCandies(3, 3))
print(s.distributeCandies2(5, 2))
print(s.distributeCandies2(3, 3))
