from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            cur = ''
            for c in word:
                if c == separator:
                    if len(cur):
                        res.append(cur)
                        cur = ''
                else:
                    cur += c
            if len(cur):
                res.append(cur)
        return res

    def splitWordsBySeparator2(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            splits = word.split(separator)
            for x in splits:
                if x != '':
                    res.append(x)
        return res


s = Solution()
print(s.splitWordsBySeparator(words=["one.two.three", "four.five", "six"], separator="."))
print(s.splitWordsBySeparator(words=["$easy$", "$problem$"], separator="$"))
print(s.splitWordsBySeparator(words=["|||"], separator="|"))
print(s.splitWordsBySeparator2(words=["one.two.three", "four.five", "six"], separator="."))
print(s.splitWordsBySeparator2(words=["$easy$", "$problem$"], separator="$"))
print(s.splitWordsBySeparator2(words=["|||"], separator="|"))
