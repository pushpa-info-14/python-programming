class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = []
        for c in s:
            val = ord(c) - ord('a') + 1
            if val < 10:
                digits.append(val)
            else:
                digits.append(val // 10)
                digits.append(val % 10)
        res = sum(digits)
        for i in range(1, k):
            cur = 0
            x = res
            while x:
                cur += x % 10
                x //= 10
            res = cur
        return res


s = Solution()
print(s.getLucky(s="iiii", k=1))
print(s.getLucky(s="leetcode", k=2))
print(s.getLucky(s="zbax", k=2))
