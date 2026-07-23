class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n & 1:
            return 2 * n
        return n


s = Solution()
print(s.smallestEvenMultiple(5))
print(s.smallestEvenMultiple(6))
