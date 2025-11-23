class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        start = n % k
        res = ""
        if start > 0:
            res += s[:start]
        else:
            res += s[:k]
            start = k

        for i in range(start, n, k):
            res += "-" + s[i:i + k]
        return res


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
