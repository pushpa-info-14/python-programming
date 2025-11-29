from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        counter = Counter(s1.split(' ') + s2.split(' '))
        for word in counter.keys():
            if counter[word] == 1:
                res.append(word)
        return res


s = Solution()
print(s.uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour"))
print(s.uncommonFromSentences(s1="apple apple", s2="banana"))
