class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, arr)

    def _build(self, node, low, high, arr):
        if low == high:
            self.tree[node] = arr[low]
        else:
            mid = (low + high) // 2
            self._build(node * 2 + 1, low, mid, arr)
            self._build(node * 2 + 2, mid + 1, high, arr)
            self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def _push(self, node, low, high):
        if self.lazy[node] != 0:
            self.tree[node] += (high - low + 1) * self.lazy[node]
            if low != high:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

    def _query(self, node, low, high, l, r):
        self._push(node, low, high)

        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return 0
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.tree[node]
        # Partial overlap
        mid = (low + high) // 2
        left = self._query(node * 2 + 1, low, mid, l, r)
        right = self._query(node * 2 + 2, mid + 1, high, l, r)
        return left + right

    def _update(self, node, low, high, l, r, val):
        self._push(node, low, high)

        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            self.lazy[node] += val
            self._push(node, low, high)
            return
        # Partial overlap
        mid = (low + high) // 2
        self._update(node * 2 + 1, low, mid, l, r, val)
        self._update(node * 2 + 2, mid + 1, high, l, r, val)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def update(self, l, r, val):
        self._update(0, 0, self.n - 1, l, r, val)


nums = [1, 3, 5, 7, 9, 11]
st = SegmentTree(nums)
print(st.query(1, 3))  # 3 + 5 + 7 = 15
st.update(1, 4, 10)  # Add 10 to indices [1..4]
print(st.query(1, 3))  # (3 + 10) + (5 + 10) + (7 + 10) = 45
print(st.query(4, 4))  # 9 + 10 = 19
