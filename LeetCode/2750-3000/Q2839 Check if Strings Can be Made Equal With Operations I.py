class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)

        for i in range(2):
            if s1[i] > s1[i + 2]:
                s1[i], s1[i + 2] = s1[i + 2], s1[i]
            if s2[i] > s2[i + 2]:
                s2[i], s2[i + 2] = s2[i + 2], s2[i]
        return s1 == s2


s = Solution()
print(s.canBeEqual(s1="abcd", s2="cdab"))
print(s.canBeEqual(s1="abcd", s2="dacb"))
