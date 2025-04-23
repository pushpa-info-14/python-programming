from typing import List


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size + 1)

    def _build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
            return

        tm = (tl + tr) // 2
        self._build(arr, 2 * v, tl, tm)
        self._build(arr, 2 * v + 1, tm + 1, tr)
        self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

    def _query(self, v, tl, tr, k):
        if self.tree[v] < k:
            return -1
        if tl == tr:
            self.tree[v] = -1
            return tl

        tm = (tl + tr) // 2
        if self.tree[2 * v] >= k:
            index = self._query(2 * v, tl, tm, k)
        else:
            index = self._query(2 * v + 1, tm + 1, tr, k)
        self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])
        return index

    def build(self, arr):
        self._build(arr, 1, 0, self.size - 1)

    def query(self, k):
        return self._query(1, 0, self.size - 1, k)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        st = SegmentTree(n)
        st.build(baskets)
        unplaced = 0

        for fruit in fruits:
            if st.query(fruit) == -1:
                unplaced += 1
        return unplaced


s = Solution()
print(s.numOfUnplacedFruits(fruits=[4, 2, 5], baskets=[3, 5, 4]))
print(s.numOfUnplacedFruits(fruits=[3, 6, 1], baskets=[6, 4, 7]))
