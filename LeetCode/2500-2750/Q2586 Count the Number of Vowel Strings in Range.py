from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set(list("aeiou"))
        res = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                res += 1
        return res


s = Solution()
print(s.vowelStrings(words=["are", "amy", "u"], left=0, right=2))
print(s.vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4))
