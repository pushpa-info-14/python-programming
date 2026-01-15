class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, node * 2, start, mid)
            self._build(arr, node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _update(self, node, start, end, l, r, val):
        self._push(node, start, end)

        # No overlap [l r start end] [start end l r]
        if r < start or end < l:
            return
        # Complete overlap [l start end r]
        if l <= start and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return

        mid = (start + end) // 2
        self._update(node * 2, start, mid, l, r, val)
        self._update(node * 2 + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node, start, end, l, r):
        self._push(node, start, end)

        if r < start or end < l:
            return 0

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        return (
                self._query(node * 2, start, mid, l, r) +
                self._query(node * 2 + 1, mid + 1, end, l, r)
        )

    def update(self, l, r, val):
        self._update(1, 0, self.n - 1, l, r, val)

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)


nums = [1, 3, 5, 7, 9, 11]
st = SegmentTree(nums)
print(st.query(1, 3))  # 3 + 5 + 7 = 15
st.update(1, 4, 10)  # Add 10 to indices [1..4]
print(st.query(1, 3))  # (3 + 10) + (5 + 10) + (7 + 10) = 45
print(st.query(4, 4))  # 9 + 10 = 19
