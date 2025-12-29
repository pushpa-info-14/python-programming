from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed = set(allowed)
        chars = set([j[2] for j in allowed])
        n = len(bottom)

        def possibilities(string):
            p = [[] for _ in range(len(string) - 1)]
            for i in range(len(p)):
                a, b = string[i], string[i + 1]
                for c in chars:
                    if a + b + c in allowed:
                        p[i].append(c)
            patterns = {''}
            for i in range(len(p)):
                temp = set()
                for string in patterns:
                    for c in p[i]:
                        temp.add(string + c)
                patterns = temp
            return patterns

        prev = {bottom}
        for j in range(n):
            cur = set()
            for k in prev:
                if j == n - 1 and len(k) == 1:
                    return True
                cur |= possibilities(k)
            prev = cur
        return False


s = Solution()
print(s.pyramidTransition(bottom="BCD", allowed=["BCC", "CDE", "CEA", "FFF"]))
print(s.pyramidTransition(bottom="AAAA", allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]))
print(s.pyramidTransition(bottom="DEFC", allowed=["DEB", "EFC", "FCB", "BCA", "CBD"]))
print(s.pyramidTransition(bottom="DBCBBC",
                          allowed=["AAD", "ACB", "AAA", "AAC", "AAB", "BCD", "BCA", "BCC", "BAB", "BAC", "BAA", "CAC",
                                   "CAB", "CAA", "CCC", "DAD", "BDD", "CCD", "DAA", "DAC", "ACD", "DCC", "ACC", "ABA",
                                   "ABB", "ABC", "ABD", "BDC", "BDB", "BBD", "BBC", "BBB", "ADD", "ADB", "ADC", "ADA",
                                   "DDC", "DDA", "CBB", "CBC", "CBA", "CDA", "CBD", "CDC", "DBA", "DBC"]))
