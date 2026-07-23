class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # Base case for n = 1
        aba = 6
        abc = 6
        for _ in range(n - 1):
            next_aba = (3 * aba + 2 * abc) % mod
            next_abc = (2 * aba + 2 * abc) % mod
            aba = next_aba
            abc = next_abc
        return (aba + abc) % mod


s = Solution()
print(s.numOfWays(1))
print(s.numOfWays(5000))
