class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        chars = list(s)
        i = 0
        j = k - 1
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return "".join(chars)


s = Solution()
print(s.reversePrefix(s="abcd", k=2))
print(s.reversePrefix(s="xyz", k=3))
print(s.reversePrefix(s="hey", k=1))
