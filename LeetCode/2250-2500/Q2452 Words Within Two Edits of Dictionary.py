from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []
        for query in queries:
            for word in dictionary:
                count = 0
                for i in range(n):
                    if query[i] != word[i]:
                        count += 1
                        if count > 2:
                            break
                if count <= 2:
                    res.append(query)
                    break
        return res


s = Solution()
print(s.twoEditWords(queries=["word", "note", "ants", "wood"], dictionary=["wood", "joke", "moat"]))
print(s.twoEditWords(queries=["yes"], dictionary=["not"]))
print(s.twoEditWords(queries=["tsl", "sri", "yyy", "rbc", "dda", "qus", "hyb", "ilu", "ahd"],
                     dictionary=["uyj", "bug", "dba", "xbe", "blu", "wuo", "tsf", "tga"]))
