from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        values = sorted(freq.values())
        n = len(word)
        res = n

        for i in range(len(values)):
            current = 0
            for j in range(len(values)):
                if values[i] > values[j]:
                    current += values[j]
                if values[i] + k < values[j]:
                    current += (values[j] - (values[i] + k))
            res = min(res, current)
        return res


s = Solution()
print(s.minimumDeletions(word="aabcaba", k=0))
print(s.minimumDeletions(word="dabdcbdcdcd", k=2))
print(s.minimumDeletions(word="aaabaaa", k=2))
