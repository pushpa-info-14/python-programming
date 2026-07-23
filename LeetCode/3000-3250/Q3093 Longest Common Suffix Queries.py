from typing import List


class TrieNode:
    def __init__(self, smallest=10 ** 10, index=10 ** 10):
        self.children = {}
        self.smallest = smallest
        self.index = index


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, i: int, word: str) -> None:
        cur = self.root
        if cur.smallest > len(word):
            cur.smallest = len(word)
            cur.index = i
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(len(word), i)
            cur = cur.children[c]
            if cur.smallest > len(word):
                cur.smallest = len(word)
                cur.index = i

    def query(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return cur.index
            cur = cur.children[c]
        return cur.index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(i, word[::-1])
        res = []
        for word in wordsQuery:
            res.append(trie.query(word[::-1]))
        return res


s = Solution()
print(s.stringIndices(wordsContainer=["abcd", "bcd", "xbcd"], wordsQuery=["cd", "bcd", "xyz"]))
print(s.stringIndices(wordsContainer=["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"]))
