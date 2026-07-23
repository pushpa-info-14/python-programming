class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp = {}
        res = 0
        for i in range(len(s)):
            mp[s[i]] = i
        for i in range(len(t)):
            res += abs(mp[t[i]] - i)
        return res


s = Solution()
print(s.findPermutationDifference(s="abc", t="bac"))
print(s.findPermutationDifference(s="abcde", t="edbac"))
