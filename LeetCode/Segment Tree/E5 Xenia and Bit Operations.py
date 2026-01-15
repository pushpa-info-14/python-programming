import math
from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.is_or = int(math.log2(self.n)) % 2 == 1
        self._build(0, 0, self.n - 1, arr, self.is_or)

    def _build(self, node, low, high, arr, is_or):
        if low == high:
            self.tree[node] = arr[low]
        else:
            mid = (low + high) // 2
            self._build(2 * node + 1, low, mid, arr, not is_or)
            self._build(2 * node + 2, mid + 1, high, arr, not is_or)

            if is_or:
                self.tree[node] = self.tree[2 * node + 1] | self.tree[2 * node + 2]
            else:
                self.tree[node] = self.tree[2 * node + 1] ^ self.tree[2 * node + 2]

    def _query(self, node, low, high, l, r, is_or):
        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return 0
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.tree[node]
        # Partial overlap
        mid = (low + high) // 2
        left = self._query(2 * node + 1, low, mid, l, r, not is_or)
        right = self._query(2 * node + 2, mid + 1, high, l, r, not is_or)

        if is_or:
            return left | right
        else:
            return left ^ right

    def _update(self, node, low, high, index, val, is_or):
        if low == high:
            self.tree[node] = val
        else:
            mid = (low + high) // 2
            if index <= mid:
                self._update(2 * node + 1, low, mid, index, val, not is_or)
            else:
                self._update(2 * node + 2, mid + 1, high, index, val, not is_or)

            if is_or:
                self.tree[node] = self.tree[2 * node + 1] | self.tree[2 * node + 2]
            else:
                self.tree[node] = self.tree[2 * node + 1] ^ self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r, self.is_or)

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value, self.is_or)


class Solution:
    def bitOperations(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums)
        res = []
        for index, val in queries:
            # 1 based indexing
            st.update(index - 1, val)
            res.append(st.query(0, n - 1))
        return res


s = Solution()
print(s.bitOperations([1, 6, 3, 5], [[1, 4], [3, 4], [1, 2], [1, 2]]))  # [1, 3, 3, 3]
