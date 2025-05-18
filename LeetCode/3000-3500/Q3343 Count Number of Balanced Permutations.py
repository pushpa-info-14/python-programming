class Solution:
    MOD = 10 ** 9 + 7

    def modMul(self, a, b):
        return (a % self.MOD) * (b % self.MOD) % self.MOD

    def computeFactorial(self, n):
        self.fact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = self.modMul(self.fact[i - 1], i)

    def binaryExponentiation(self, a, b):
        res = 1
        while b > 0:
            if b & 1:
                res = self.modMul(res, a)
            a = self.modMul(a, a)
            b >>= 1
        return res

    def computeInverseFactorial(self, n):
        self.inverse_fact = [1] * (n + 1)
        for i in range(n + 1):
            self.inverse_fact[i] = self.binaryExponentiation(self.fact[i], self.MOD - 2)

    def countPermutation(self, digit, leftover, target):
        if digit == 10:
            return self.tot_ways_to_permute if (leftover == 0 and target == 0) else 0
        if self.mem[digit][leftover][target] != -1:
            return self.mem[digit][leftover][target]

        include_count = min(leftover, self.freq[digit])
        if digit > 0:
            include_count = min(include_count, target // digit)

        ans = 0
        for i in range(include_count + 1):
            ways_for_current_digit = self.modMul(self.inverse_fact[i], self.inverse_fact[self.freq[digit] - i])
            ans += ways_for_current_digit * self.countPermutation(digit + 1, leftover - i, target - digit * i)
            ans %= self.MOD
        self.mem[digit][leftover][target] = ans
        return ans

    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        sum_digits = 0
        self.freq = [0] * 10
        for ch in num:
            digit = int(ch)
            sum_digits += digit
            self.freq[digit] += 1

        if sum_digits % 2 == 1:
            return 0

        target = sum_digits // 2
        self.computeFactorial(n)
        self.computeInverseFactorial(n)

        half_len = n // 2
        self.tot_ways_to_permute = self.modMul(self.fact[half_len], self.fact[n - half_len])

        # Initialize memoization table
        max_sum = 42 * 9  # As per the C++ code's comment
        self.mem = [[[-1] * (max_sum + 1) for _ in range(half_len + 1)] for _ in range(10)]

        return self.countPermutation(0, half_len, target)


s = Solution()
print(s.countBalancedPermutations("123"))
print(s.countBalancedPermutations("112"))
print(s.countBalancedPermutations("12345"))
