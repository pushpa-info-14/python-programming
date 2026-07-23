class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        splits = [i for i in p.split('*') if len(i) > 0]
        if len(splits) == 0:
            return True
        elif len(splits) == 1:
            return splits[0] in s
        else:
            idx1 = s.find(splits[0])
            if idx1 == -1: return False
            idx2 = s.rfind(splits[1])
            if idx2 == -1: return False
            return idx1 + len(splits[0]) <= idx2


s = Solution()
print(s.hasMatch(s="leetcode", p="ee*e"))  # True
print(s.hasMatch(s="car", p="c*v"))  # False
print(s.hasMatch(s="luck", p="u*"))  # True
print(s.hasMatch(s="kvb", p="k*v"))  # True
print(s.hasMatch(s="hccc", p="m*c"))  # False
print(s.hasMatch(s="sjjsjjssjss", p="jss*sj"))  # False
