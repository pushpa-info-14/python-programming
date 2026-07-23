from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        res = ''
        flip = False
        while counter:
            for c in sorted(counter.keys(), reverse=flip):
                res += c
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            flip = not flip
        return res


s = Solution()
print(s.sortString(s="aaaabbbbcccc"))
print(s.sortString(s="rat"))
