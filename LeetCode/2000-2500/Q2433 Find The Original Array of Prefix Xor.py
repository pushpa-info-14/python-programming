from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i - 1] ^ pref[i])
        return res


s = Solution()
print(s.findArray(pref=[5, 2, 0, 3, 1]))
print(s.findArray(pref=[13]))
