from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
        for c in "!?',;.":
            p = p.replace(c, ' ')
        words = p.split()
        banned_words = set(banned)
        counter = Counter(words)
        max_count = 0
        max_word = ''
        for word in words:
            if word not in banned_words:
                if max_count < counter[word]:
                    max_count = counter[word]
                    max_word = word
        return max_word


s = Solution()
print(s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
print(s.mostCommonWord(paragraph="a.", banned=[]))
print(s.mostCommonWord(paragraph="a b.b", banned=[]))
