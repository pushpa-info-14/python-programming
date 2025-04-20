from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def getMax(self, num):
        node = self.root
        max_num = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if 1 - bit in node.children:
                max_num |= 1 << i
                node = node.children[1 - bit]
            else:
                node = node.children[bit]
        return max_num


def maxXOR(arr1: List[int], arr2: List[int]):
    trie = Trie()
    for num in arr1:
        trie.insert(num)

    max_num = 0
    for num in arr2:
        max_num = max(max_num, trie.getMax(num))
    return max_num


"""
Given an array of numbers, and a number x. Find the max value of array[i]^x
"""

print(maxXOR([6, 8], [7, 8, 2]))
print(maxXOR([1, 2], [1, 1]))
