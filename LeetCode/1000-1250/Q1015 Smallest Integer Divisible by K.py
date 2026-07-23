class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur = 0
        for i in range(k):
            cur = (cur * 10 + 1) % k
            if cur == 0:
                return i + 1
        return -1


s = Solution()
print(s.smallestRepunitDivByK(1))
print(s.smallestRepunitDivByK(2))
print(s.smallestRepunitDivByK(3))
