class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> int:
        cur = self.root
        count = 0
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                count += 1
            cur = cur.children[c]
        return count


def countDistinct(s: str) -> int:
    n = len(s)
    res = 0
    trie = Trie()
    for i in range(n):
        w = ""
        for j in range(i, n):
            w += s[j]
        res += trie.insert(w)
    return res


print(countDistinct("abab"))
print(countDistinct("ab"))
print(countDistinct("a"))
