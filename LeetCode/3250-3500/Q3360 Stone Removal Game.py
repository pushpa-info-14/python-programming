class Solution:
    def canAliceWin(self, n: int) -> bool:
        is_alice = False
        for i in range(10, 0, -1):
            if n - i < 0:
                return is_alice
            n -= i
            is_alice = not is_alice
        return is_alice


s = Solution()
print(s.canAliceWin(12))
print(s.canAliceWin(1))
