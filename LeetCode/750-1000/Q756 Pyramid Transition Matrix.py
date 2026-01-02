from collections import defaultdict
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for p in allowed:
            lr = p[:2]
            t = p[2:]
            mp[lr].append(t)
        n = len(bottom)

        def possibilities(string):
            p = [[] for _ in range(len(string) - 1)]
            for i in range(len(p)):
                x = string[i:i + 2]
                if x in mp:
                    for y in mp[x]:
                        p[i].append(y)
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

    def pyramidTransition2(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for temp in allowed:
            lr = temp[:2]
            t = temp[2:]
            mp[lr].append(t)
        memo = {}

        def dfs(last, cur, i, n):
            if n == 0:  # Built pyramid
                return True
            if i == n:  # Finished current row
                key = "".join(cur)
                if key in memo:
                    return memo[key]
                memo[key] = dfs(cur, [], 0, n - 1)
                return memo[key]
            a, b = last[i], last[i + 1]
            for c in mp[a + b]:
                cur.append(c)
                if dfs(last, cur, i + 1, n):
                    return True
                cur.pop()
            return False

        return dfs(list(bottom), [], 0, len(bottom) - 1)


s = Solution()
print(s.pyramidTransition(bottom="BCD", allowed=["BCC", "CDE", "CEA", "FFF"]))
print(s.pyramidTransition(bottom="AAAA", allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]))
print(s.pyramidTransition(bottom="DEFC", allowed=["DEB", "EFC", "FCB", "BCA", "CBD"]))
print(s.pyramidTransition(bottom="DBCBBC",
                          allowed=["AAD", "ACB", "AAA", "AAC", "AAB", "BCD", "BCA", "BCC", "BAB", "BAC", "BAA", "CAC",
                                   "CAB", "CAA", "CCC", "DAD", "BDD", "CCD", "DAA", "DAC", "ACD", "DCC", "ACC", "ABA",
                                   "ABB", "ABC", "ABD", "BDC", "BDB", "BBD", "BBC", "BBB", "ADD", "ADB", "ADC", "ADA",
                                   "DDC", "DDA", "CBB", "CBC", "CBA", "CDA", "CBD", "CDC", "DBA", "DBC"]))
print("---------------------------------")
print(s.pyramidTransition2(bottom="BCD", allowed=["BCC", "CDE", "CEA", "FFF"]))
print(s.pyramidTransition2(bottom="AAAA", allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]))
print(s.pyramidTransition2(bottom="DEFC", allowed=["DEB", "EFC", "FCB", "BCA", "CBD"]))
print(s.pyramidTransition2(bottom="DBCBBC",
                           allowed=["AAD", "ACB", "AAA", "AAC", "AAB", "BCD", "BCA", "BCC", "BAB", "BAC", "BAA", "CAC",
                                    "CAB", "CAA", "CCC", "DAD", "BDD", "CCD", "DAA", "DAC", "ACD", "DCC", "ACC", "ABA",
                                    "ABB", "ABC", "ABD", "BDC", "BDB", "BBD", "BBC", "BBB", "ADD", "ADB", "ADC", "ADA",
                                    "DDC", "DDA", "CBB", "CBC", "CBA", "CDA", "CBD", "CDC", "DBA", "DBC"]))
