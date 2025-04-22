class Solution:
    def idealArrays(self, n: int, max_value: int) -> int:
        mod = 10 ** 9 + 7
        count = [[0] * 10005 for _ in range(15)]
        prefix_sum = [[0] * 10005 for _ in range(15)]
        options = [0] * 15

        def countUniqueSequences(curr, idx):
            options[idx] += 1
            fact = 2
            while curr * fact <= max_value:
                countUniqueSequences(curr * fact, idx + 1)
                fact += 1

        # Pre-fill 1st row
        for i in range(1, 10001):
            count[1][i] = 1
            prefix_sum[1][i] = i

        # Fill the count table
        for i in range(2, 15):
            for j in range(i, 10001):
                count[i][j] = prefix_sum[i - 1][j - 1]
                prefix_sum[i][j] = (count[i][j] + prefix_sum[i][j - 1]) % mod
                count[i][j] %= mod

        # Calculate options
        for i in range(1, max_value + 1):
            countUniqueSequences(i, 1)

        # Count total ideal arrays
        ans = 0
        for i in range(1, 15):
            ways = (count[i][n] * options[i]) % mod
            ans = (ans + ways) % mod
        return ans


s = Solution()
print(s.idealArrays(n=2, max_value=5))
print(s.idealArrays(n=5, max_value=3))
