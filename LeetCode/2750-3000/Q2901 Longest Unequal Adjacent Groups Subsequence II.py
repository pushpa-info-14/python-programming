from typing import List


def hamming(str1, str2):
    n = len(str1)
    distance = 0
    for i in range(n):
        if str1[i] != str2[i]:
            distance += 1
    return distance


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[words[i]] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming(words[i], words[j]) == 1:
                    if len(dp[i]) < len(dp[j]) + 1:
                        copy = dp[j].copy()
                        copy.append(words[i])
                        dp[i] = copy

        res = []
        for elements in dp:
            if len(res) < len(elements):
                res = elements
        return res


s = Solution()
print(s.getWordsInLongestSubsequence(words=["bab", "dab", "cab"], groups=[1, 2, 2]))
print(s.getWordsInLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]))
print(s.getWordsInLongestSubsequence(words=["bab", "bdd", "bca", "dab"], groups=[2, 4, 1, 2]))
print(s.getWordsInLongestSubsequence(words=["ca", "cb", "bcd", "bb", "ddc"], groups=[2, 4, 2, 5, 1]))
print(s.getWordsInLongestSubsequence(words=["bcb", "cba", "cab", "cca", "ad", "cd"], groups=[6, 5, 1, 5, 5, 1]))
