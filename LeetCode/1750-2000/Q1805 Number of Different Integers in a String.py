class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        cur = ''
        seen = set()
        for c in word:
            if c.isdigit():
                cur += c
            else:
                if cur:
                    seen.add(int(cur))
                    cur = ''
        if cur:
            seen.add(int(cur))
        return len(seen)


s = Solution()
print(s.numDifferentIntegers(word="a123bc34d8ef34"))
print(s.numDifferentIntegers(word="leet1234code234"))
print(s.numDifferentIntegers(word="a1b01c001"))
