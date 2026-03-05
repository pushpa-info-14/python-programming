from collections import defaultdict
from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        mp = defaultdict(int)
        for word in words:
            if len(word) >= k:
                mp[word[:k]] += 1
        res = 0
        for val in mp.values():
            if val >= 2:
                res += 1
        return res


s = Solution()
print(s.prefixConnected(words=["apple", "apply", "banana", "bandit"], k=2))
print(s.prefixConnected(words=["car", "cat", "cartoon"], k=3))
print(s.prefixConnected(words=["bat", "dog", "dog", "doggy", "bat"], k=3))
