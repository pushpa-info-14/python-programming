from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        processed = []
        for word in words:
            processed.append(''.join(sorted(set(list(word)))))
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if processed[i] == processed[j]:
                    res += 1
        return res


s = Solution()
print(s.similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"]))
print(s.similarPairs(words=["aabb", "ab", "ba"]))
print(s.similarPairs(words=["nba", "cba", "dba"]))
