from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: List[str]) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            if cur.flag:
                return False
        cur.flag = True
        return True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        res = []
        for f in folder:
            if trie.insert(f.split('/')):
                res.append(f)
        return res


s = Solution()
print(s.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(s.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))
print(s.removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]))
