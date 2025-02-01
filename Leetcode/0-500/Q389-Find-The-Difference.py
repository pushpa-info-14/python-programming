class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for i in set(s):
            seen[i] = s.count(i)

        for i in t:
            if i not in seen or seen[i] == 0:
                return i
            seen[i] -= 1
        return ""

    def findTheDifference2(self, s: str, t: str) -> str:
        s += t
        res = 0
        for i in s:
            res ^= ord(i)
        return chr(res)


s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference2("abcd", "abcde"))
print(s.findTheDifference2("a", "aa"))
