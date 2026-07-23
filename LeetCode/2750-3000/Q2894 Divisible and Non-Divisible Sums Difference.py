class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        range_sum = (n * (n + 1)) // 2

        divisible_sum = 0
        for i in range(m, n + 1, m):
            divisible_sum += i

        none_divisible_sum = range_sum - divisible_sum

        return none_divisible_sum - divisible_sum


s = Solution()
print(s.differenceOfSums(n=10, m=3))
print(s.differenceOfSums(n=5, m=6))
print(s.differenceOfSums(n=5, m=1))
