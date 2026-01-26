from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        res = 0
        for key, value in counter1.items():
            if value == 1 and key in counter2 and counter2[key] == 1:
                res += 1
        return res


s = Solution()
print(s.countWords(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
print(s.countWords(words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
print(s.countWords(words1=["a", "ab"], words2=["a", "a", "a", "ab"]))
