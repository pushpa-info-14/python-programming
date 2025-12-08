from collections import defaultdict


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        counter = defaultdict(int)
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            while r - l + 1 > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            if r - l + 1 == k:
                flag = True
                if len(counter.keys()) != 1:
                    flag = False
                if l - 1 >= 0 and s[l - 1] in counter:
                    flag = False
                if r + 1 < n and s[r + 1] in counter:
                    flag = False
                if flag:
                    return True
        return False


s = Solution()
print(s.hasSpecialSubstring(s="aaabaaa", k=3))
print(s.hasSpecialSubstring(s="abc", k=2))
