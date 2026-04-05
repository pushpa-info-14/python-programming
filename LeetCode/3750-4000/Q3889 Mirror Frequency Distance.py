from collections import Counter


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for c in set(s):
            if c.isalpha():
                gap = ord(c) - ord("a")
                mirror = chr(ord('z') - gap)
            else:
                gap = ord(c) - ord("0")
                mirror = chr(ord('9') - gap)
            res += abs(counter[c] - counter[mirror])
            counter[c] = 0
            counter[mirror] = 0
        return res


s = Solution()
print(s.mirrorFrequency(s="ab1z9"))
print(s.mirrorFrequency(s="4m7n"))
print(s.mirrorFrequency(s="byby"))
