from functools import cache

MAX_LEN = 200
DIVISORS = [[1] for _ in range(MAX_LEN + 1)]
for d in range(2, MAX_LEN + 1):
    for num in range(d, MAX_LEN + 1, d):
        DIVISORS[num].append(d)


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = 10 ** 10

        @cache
        def changes_pal(start, pal_len, d):
            if pal_len == 1:
                return 0
            if pal_len == 2:
                return 0 if s[start] == s[start + d] else 1
            return (0 if s[start] == s[start + (d * (pal_len - 1))] else 1) + changes_pal(start + d, pal_len - 2, d)

        @cache
        def to_semipal(start, end):
            string_len = end - start
            best = inf
            for d in DIVISORS[string_len]:
                if d == string_len:
                    break
                group_len = string_len // d
                changes = 0
                for i in range(d):
                    changes += changes_pal(start + i, group_len, d)
                best = min(best, changes)
            return best

        @cache
        def dp(i, parts):
            if parts == 1:
                return to_semipal(i, n)
            best = inf
            for j in range(i + 2, n - (2 * (parts - 1)) + 1):
                best = min(best, to_semipal(i, j) + dp(j, parts - 1))
            return best

        return dp(0, k)

s = Solution()
print(s.minimumChanges(s = "abcac", k = 2))
print(s.minimumChanges(s = "abcdef", k = 2))
print(s.minimumChanges(s = "aabbaa", k = 3))
