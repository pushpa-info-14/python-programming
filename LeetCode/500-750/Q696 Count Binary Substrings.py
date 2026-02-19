class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        prev = s[0]
        for b in s[1:]:
            if b == prev:
                count += 1
            else:
                groups.append(count)
                prev = b
                count = 1
        groups.append(count)

        res = 0
        for i in range(len(groups) - 1):
            res += min(groups[i], groups[i + 1])
        return res


s = Solution()
print(s.countBinarySubstrings(s="00110011"))
print(s.countBinarySubstrings(s="10101"))
