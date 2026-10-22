class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        is_sorted = True
        min_c = s[0]
        max_c = s[0]
        for i in range(1, n):
            min_c = min(min_c, s[i])
            max_c = max(max_c, s[i])
            if s[i - 1] > s[i]:
                is_sorted = False
        if is_sorted:
            return 0
        if n == 2:
            return -1
        if min_c == s[0] or max_c == s[-1]:
            return 1
        for c in s[1:n - 1]:
            if c == min_c or c == max_c:
                return 2
        return 3


s = Solution()
print(s.minOperations(s = "dog"))
print(s.minOperations(s = "card"))
print(s.minOperations(s = "gf"))
print(s.minOperations(s="edc"))
