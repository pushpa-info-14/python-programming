class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        n = len(s)
        for i in range(n - k + 1):
            seen.add(int(s[i:i + k], 2))
        return len(seen) == 2 ** k


s = Solution()
print(s.hasAllCodes(s="00110110", k=2))
print(s.hasAllCodes(s="0110", k=1))
print(s.hasAllCodes(s="0110", k=2))
