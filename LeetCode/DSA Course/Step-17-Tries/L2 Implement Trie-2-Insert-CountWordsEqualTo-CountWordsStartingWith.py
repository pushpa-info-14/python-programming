class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_with = 0
        self.prefix_count = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefix_count += 1
        cur.end_with += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.end_with

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.prefix_count

    def erase(self, word: str) -> None: # Assuming the word is already in the trie
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.prefix_count -= 1
            else:
                return
        cur.end_with -= 1


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.insert("apple")
print(trie.countWordsEqualTo("apple"))
print(trie.countWordsEqualTo("app"))
print(trie.countWordsStartingWith("app"))
print(trie.countWordsStartingWith("xpp"))
trie.insert("app")
print(trie.countWordsEqualTo("app"))
print(trie.countWordsStartingWith("app"))
trie.erase("app")
print(trie.countWordsEqualTo("app"))
print(trie.countWordsStartingWith("app"))
