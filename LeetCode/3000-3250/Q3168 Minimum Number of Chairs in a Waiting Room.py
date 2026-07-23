class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        empty = 0

        for c in s:
            if c == 'E':
                if empty:
                    empty -= 1
                else:
                    chairs += 1
            else:
                empty += 1
        return chairs


s = Solution()
print(s.minimumChairs(s="EEEEEEE"))
print(s.minimumChairs(s="ELELEEL"))
print(s.minimumChairs(s="ELEELEELLL"))
