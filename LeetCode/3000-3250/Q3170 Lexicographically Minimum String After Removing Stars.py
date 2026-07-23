from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        freq = defaultdict(list)

        ss = list(s)
        mini = "z"
        for i, c in enumerate(s):
            if c != "*":
                mini = min(mini, c)
                freq[c].append(i)
            else:
                ss[freq[mini][-1]] = "*"
                del freq[mini][-1]
                if len(freq[mini]) == 0:
                    del freq[mini]
                    mini = 'z'
                    for key in freq.keys():
                        mini = min(mini, key)

        res = ""
        for c in ss:
            if c != "*":
                res += c
        return res


s = Solution()
print(s.clearStars("aaba*"))
print(s.clearStars("abc"))
print(s.clearStars("d*c"))
print(s.clearStars("d*o*"))
print(s.clearStars("d*yed"))
print(s.clearStars("edy*y*"))
