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


def maxXorQueries(arr: List[int], queries: List[List[int]]):
    arr.sort()
    res = [-1] * len(queries)
    offline_queries = []
    for i, query in enumerate(queries):
        offline_queries.append((query[1], query[0], i))

    # QlogQ
    offline_queries.sort()
    trie = Trie()
    j = 0
    # Q*32 + N*32
    for i in range(len(offline_queries)):
        ai, xi, index = offline_queries[i]
        while j < len(arr) and arr[j] <= ai:
            trie.insert(arr[j])
            j += 1
        if j != 0: # Trie is not empty
            maximum = trie.getMax(xi)
            res[index] = maximum

    return res


print(maxXorQueries([0, 1, 2, 3, 4], [[1, 3], [5, 6]]))
print(maxXorQueries([1], [[1, 0]]))
