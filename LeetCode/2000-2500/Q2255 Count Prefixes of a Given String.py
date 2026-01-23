from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if word == s[:len(word)]:
                res += 1
        return res


s = Solution()
print(s.countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
print(s.countPrefixes(words=["a", "a"], s="aa"))
