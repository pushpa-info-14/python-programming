from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for x in strs:
            if x.isnumeric():
                res = max(res, int(x))
            else:
                res = max(res, len(x))
        return res


s = Solution()
print(s.maximumValue(strs=["alic3", "bob", "3", "4", "00000"]))
print(s.maximumValue(strs=["1", "01", "001", "0001"]))
