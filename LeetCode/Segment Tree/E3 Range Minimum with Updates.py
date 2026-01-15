from typing import List


class SegmentTree:
    _inf = 10 ** 10

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, arr)

    def _build(self, node, low, high, arr):
        if low == high:
            self.tree[node] = arr[low]
        else:
            mid = (low + high) // 2
            self._build(2 * node + 1, low, mid, arr)
            self._build(2 * node + 2, mid + 1, high, arr)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node, low, high, l, r):
        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return self._inf
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.tree[node]
        # Partial overlap
        mid = (low + high) // 2
        left = self._query(2 * node + 1, low, mid, l, r)
        right = self._query(2 * node + 2, mid + 1, high, l, r)
        return min(left, right)

    def _update(self, node, low, high, index, val):
        if low == high:
            self.tree[node] = val
        else:
            mid = (low + high) // 2
            if index <= mid:
                self._update(2 * node + 1, low, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, high, index, val)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)


class Solution:
    def rangeMin(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        st = SegmentTree(nums)
        res = []
        for x, y, z in queries:
            if x == 1:
                res.append(st.query(y, z))
            else:
                st.update(y, z)
        return res


# type 1 = query
# type 2 = update
s = Solution()
print(s.rangeMin([1, 2, 7, 1, 6, 3, 5], [[1, 1, 4], [2, 3, 4], [1, 1, 2], [2, 1, 5]]))
