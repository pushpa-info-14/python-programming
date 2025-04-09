from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

    def isComplete(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if not cur.flag:
                return False
        return True


def completeString(words: List[str]):
    words.sort()
    trie = Trie()
    for word in words:
        trie.insert(word)

    max_word = ""
    for word in words:
        if trie.isComplete(word):
            if len(max_word) < len(word):
                max_word = word

    return max_word if len(max_word) > 0 else "None"


"""
Ninja developed a love for arrays and strings so this time his teacher gave him 
an array of strings, ‘A’ of size ‘N’. Each element of this array is a string. The 
teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.

A string is called a complete string if every prefix of this string is also present 
in the array ‘A’. Ninja is challenged to find the longest complete string in the 
array ‘A’.If there are multiple strings with the same length, return the lexicographically 
smallest one and if no string exists, return "None".
"""

print(completeString(["n", "ni", "nin", "ninj", "ninja", "ninga"]))
print(completeString(["ab", "bc"]))
print(completeString(["g", "l", "lm", "ga", "lmn", "gaz"]))
