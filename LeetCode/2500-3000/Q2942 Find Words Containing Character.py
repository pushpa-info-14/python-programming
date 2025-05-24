from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for index, word in enumerate(words):
            if x in word:
                res.append(index)

        return res


s = Solution()
print(s.findWordsContaining(words=["leet", "code"], x="e"))
print(s.findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="a"))
print(s.findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="z"))
