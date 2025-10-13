from typing import List


def key(word):
    return ''.join(sorted(list(word)))


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for word in words:
            if stack and key(word) == key(stack[-1]):
                continue
            stack.append(word)
        return stack


s = Solution()
print(s.removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
print(s.removeAnagrams(words=["a", "b", "c", "d", "e"]))
