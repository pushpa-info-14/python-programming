class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        res = 0
        presses = 1
        for i in range(n // 8):
            res += 8 * presses
            presses += 1
        res += (n % 8) * presses
        return res


s = Solution()
print(s.minimumPushes(word="abcde"))
print(s.minimumPushes(word="xycdefghij"))
