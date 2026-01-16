from typing import List


class Info:
    def __init__(self):
        self.close = 0
        self.open = 0
        self.full = 0


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [Info() for _ in range(4 * self.n)]
        self._build(0, 0, self.n - 1, arr)

    @staticmethod
    def _merge(left: Info, right: Info):
        info = Info()
        info.full = left.full + right.full + min(left.open, right.close)
        info.close = left.close + right.close - min(left.open, right.close)
        info.open = left.open + right.open - min(left.open, right.close)
        return info

    def _build(self, node, low, high, arr):
        if low == high:
            info = Info()
            if arr[low] == "(":
                info.open = 1
            else:
                info.close = 1
            self.tree[node] = info
        else:
            mid = (low + high) // 2
            self._build(2 * node + 1, low, mid, arr)
            self._build(2 * node + 2, mid + 1, high, arr)
            self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node, low, high, l, r):
        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return Info()
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.tree[node]
        # Partial overlap
        mid = (low + high) // 2
        left = self._query(2 * node + 1, low, mid, l, r)
        right = self._query(2 * node + 2, mid + 1, high, l, r)
        return self._merge(left, right)

    def _update(self, node, low, high, index, val):
        if low == high:
            info = Info()
            if val == "(":
                info.open = 1
            else:
                info.close = 1
            self.tree[node] = info
        else:
            mid = (low + high) // 2
            if index <= mid:
                self._update(2 * node + 1, low, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, high, index, val)
            self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)


class Solution:
    def maxCorrectBracketSubsequence(self, s: str, queries: List[List[int]]) -> List[int]:
        arr = list(s)
        st = SegmentTree(arr)
        res = []
        for l, r in queries:
            res.append(st.query(l - 1, r - 1).full * 2)
        return res


s = Solution()
print(s.maxCorrectBracketSubsequence("())(())(())(", [[1, 1], [2, 3], [1, 2], [1, 12], [8, 12], [5, 11], [2, 10]]))
