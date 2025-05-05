class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        odd_cache = [-1] * (n + 1)
        even_cache = [-1] * (n + 1)

        def odd(num):
            if num == 0:
                return 0
            if odd_cache[num] != -1:
                return odd_cache[num]

            count = 0
            count += even(num - 1)
            count += odd(num - 1)

            odd_cache[num] = count % mod
            return odd_cache[num]

        def even(num):
            if num == 0:
                return 1

            if even_cache[num] != -1:
                return even_cache[num]

            count = 0
            count += even(num - 1)
            if num - 2 >= 0:
                count += even(num - 2)
                count += 2 * odd(num - 2)

            even_cache[num] = count % mod
            return even_cache[num]

        return even(n) % mod

    def numTilings2(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 0:
            return 0
        dp = [1, 1, 2]
        for i in range(3, n + 1):
            value = (dp[i - 3] + 2 * dp[i - 1]) % mod
            dp.append(value)
        return dp[-1]


s = Solution()
print(s.numTilings(3))
print(s.numTilings(1))
print(s.numTilings2(3))
print(s.numTilings2(1))
