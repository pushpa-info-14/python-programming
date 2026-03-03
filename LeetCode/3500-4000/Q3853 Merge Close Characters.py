from collections import Counter


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last = Counter()
        res = []
        for c in s:
            if last[c] > 0:
                continue
            last[c] += 1
            res.append(c)

            if len(res) > k:
                rem = res[-(k + 1)]
                last[rem] -= 1
        return "".join(res)


s = Solution()
print(s.mergeCharacters(s="abca", k=3))
print(s.mergeCharacters(s="aabca", k=2))
print(s.mergeCharacters(s="yybyzybz", k=2))
