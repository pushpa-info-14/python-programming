from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        valid_indexes = []
        prev = -1
        for index, group in enumerate(groups):
            if group != prev:
                valid_indexes.append(index)
            prev = group

        return [words[i] for i in valid_indexes]

    def getLongestSubsequence2(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[words[i]] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j]:
                    if len(dp[i]) < len(dp[j]) + 1:
                        copy = dp[j].copy()
                        copy.append(words[i])
                        dp[i] = copy
        res = []
        for items in dp:
            if len(res) < len(items):
                res = items
        return res


s = Solution()
print(s.getLongestSubsequence(words=["e", "a", "b"], groups=[0, 0, 1]))
print(s.getLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
print(s.getLongestSubsequence2(words=["e", "a", "b"], groups=[0, 0, 1]))
print(s.getLongestSubsequence2(words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
