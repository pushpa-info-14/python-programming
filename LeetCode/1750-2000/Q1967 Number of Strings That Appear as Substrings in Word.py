from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for pattern in patterns:
            if pattern in word:
                res += 1
        return res


s = Solution()
print(s.numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc"))
print(s.numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb"))
print(s.numOfStrings(patterns=["a", "a", "a"], word="ab"))
