from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        cur = 0
        for x in arr:
            if freq[x] == 1:
                cur += 1
            if k == cur:
                return x
        return ''


s = Solution()
print(s.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2))
print(s.kthDistinct(arr=["aaa", "aa", "a"], k=1))
print(s.kthDistinct(arr=["a", "b", "a"], k=3))
