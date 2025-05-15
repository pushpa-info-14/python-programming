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


s = Solution()
print(s.getLongestSubsequence(words=["e", "a", "b"], groups=[0, 0, 1]))
print(s.getLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
