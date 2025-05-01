from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord, 1))
        words = set(wordList)

        while q:
            word, l = q.popleft()
            for i in range(len(word)):
                chars = list(word)
                for j in range(26):
                    chars[i] = chr(j + ord('a'))
                    new_word = "".join(chars)
                    if new_word in words:
                        if new_word == endWord:
                            return l + 1
                        q.append((new_word, l + 1))
                        words.remove(new_word)

        return 0


s = Solution()
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
