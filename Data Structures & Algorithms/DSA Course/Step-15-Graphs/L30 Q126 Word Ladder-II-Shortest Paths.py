from collections import deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        q = deque()
        q.append([beginWord])
        words = set(wordList)
        res = []
        while q:
            used_on_level = set()
            for _ in range(len(q)):
                path = q.popleft()
                word = path[-1]
                if word == endWord:
                    if len(res) == 0:
                        res.append(path)
                    elif len(res[0]) == len(path):
                        res.append(path)

                for i in range(len(word)):
                    chars = list(word)
                    for j in range(26):
                        chars[i] = chr(j + ord('a'))
                        new_word = "".join(chars)
                        if new_word in words:
                            used_on_level.add(new_word)
                            path_copy = path.copy()
                            path_copy.append(new_word)
                            q.append(path_copy)

            for w in used_on_level:
                if w in words:
                    words.remove(w)
        return res


s = Solution()
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
