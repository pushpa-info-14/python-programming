from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for x in details:
            if int(x[11:13]) > 60:
                res += 1
        return res


s = Solution()
print(s.countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
print(s.countSeniors(details=["1313579440F2036", "2921522980M5644"]))
