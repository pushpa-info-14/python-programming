from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        n = len(words)
        for i in range(1, n):
            cur = Counter(words[i])
            for c in list(counter.keys()):
                if c in cur:
                    counter[c] = min(counter[c], cur[c])
                else:
                    del counter[c]
        res = []
        for c, freq in counter.items():
            res += [c] * freq
        return res


s = Solution()
print(s.commonChars(words=["bella", "label", "roller"]))
print(s.commonChars(words=["cool", "lock", "cook"]))
