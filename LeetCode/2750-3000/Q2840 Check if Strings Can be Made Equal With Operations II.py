from collections import defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        odd1, even1 = defaultdict(int), defaultdict(int)
        odd2, even2 = defaultdict(int), defaultdict(int)

        for i in range(n):
            if i & 1:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1
            else:
                even1[s1[i]] += 1
                even2[s2[i]] += 1

        return odd1 == odd2 and even1 == even2


s = Solution()
print(s.checkStrings(s1="abcdba", s2="cabdab"))
print(s.checkStrings(s1="abe", s2="bea"))
