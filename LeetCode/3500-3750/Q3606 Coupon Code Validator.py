import re
from typing import List

pattern = re.compile(r'^[A-Za-z0-9_]+$')


def validate(s):
    return bool(pattern.match(s))


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        valid_coupons = []
        for i in range(n):
            is_valid = validate(code[i])
            if not is_valid:
                continue
            is_valid = businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]
            if not is_valid:
                continue
            if isActive[i]:
                valid_coupons.append((businessLine[i], code[i]))
        valid_coupons.sort()
        return [x[1] for x in valid_coupons]


s = Solution()
print(s.validateCoupons(code=["SAVE20", "", "PHARMA5", "SAVE@20"],
                        businessLine=["restaurant", "grocery", "pharmacy", "restaurant"],
                        isActive=[True, True, True, True]))
print(s.validateCoupons(code=["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
                        businessLine=["grocery", "electronics", "invalid"], isActive=[False, True, True]))
