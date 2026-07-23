class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        chars = list(seen)
        chars.sort(reverse=True)
        for c in chars:
            if c.lower() in seen and c.upper() in seen:
                return c.upper()
        return ""


s = Solution()
print(s.greatestLetter(s="lEeTcOdE"))
print(s.greatestLetter(s="arRAzFif"))
print(s.greatestLetter(s="AbCdEfGhIjK"))
