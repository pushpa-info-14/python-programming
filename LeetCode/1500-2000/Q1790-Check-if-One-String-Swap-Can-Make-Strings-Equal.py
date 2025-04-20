class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        chars = []

        for i in range(len(s1)):
            if len(chars) > 4:
                return False
            if s1[i] != s2[i]:
                chars.append(s1[i])
                chars.append(s2[i])

        n = len(chars)
        if n == 0: return True
        if n == 4 and chars[0] == chars[3] and chars[1] == chars[2]:
            return True
        return False


s = Solution()
print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("attack", "defend"))
print(s.areAlmostEqual("kelb", "kelb"))
