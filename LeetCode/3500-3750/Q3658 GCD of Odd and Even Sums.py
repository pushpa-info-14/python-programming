class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        sum_odd = n * n  # (2 * 1 + (n - 1) * 2) * n // 2
        sum_even = n * (n + 1)  # (2 * 2 + (n - 1) * 2) * n // 2

        return gcd(sum_odd, sum_even)

    def gcdOfOddEvenSums2(self, n: int) -> int:
        return n


s = Solution()
print(s.gcdOfOddEvenSums(4))
print(s.gcdOfOddEvenSums(5))
print(s.gcdOfOddEvenSums(500))
print(s.gcdOfOddEvenSums2(4))
print(s.gcdOfOddEvenSums2(5))
print(s.gcdOfOddEvenSums2(500))
