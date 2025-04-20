from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []

        mp = defaultdict(int)
        for i in range(n):
            mp[s[i]] = i

        size = 0
        end = 0
        for i in range(n):
            size += 1
            end = max(end, mp[s[i]])
            if i == end:
                res.append(size)
                size = 0

        return res


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eccbbbbdec"))
