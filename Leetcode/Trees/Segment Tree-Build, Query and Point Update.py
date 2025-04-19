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
        self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def _query(self, v, tl, tr, l, r):
        if tr < l or tl > r:  # No overlap
            return 0
        if l <= tl and tr <= r:  # Full overlap
            return self.tree[v]

        # Partial overlap
        tm = (tl + tr) // 2
        left_ans = self._query(2 * v, tl, tm, l, r)
        right_ans = self._query(2 * v + 1, tm + 1, tr, l, r)
        return left_ans + right_ans

    def _update(self, v, tl, tr, index, val):
        if tl == index and tr == index:  # Reached leaf node
            self.tree[v] = val
            return
        if  index < tl or index > tr:
            return

        tm = (tl + tr) // 2
        self._update(2 * v, tl, tm, index, val)
        self._update(2 * v + 1, tm + 1, tr, index, val)
        self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def build(self, arr):
        self._build(arr, 1, 0, self.size - 1)

    def query(self, l, r):
        return self._query(1, 0, self.size - 1, l, r)

    def update(self, index, val):
        self._update(1, 0, self.size - 1, index, val)


nums = [1, 2, 1, 4, 2, 3, 1, 1]
n = len(nums)
segmentTree = SegmentTree(n)
segmentTree.build(nums)

for i in range(n):
    print(segmentTree.query(i, i))

summation = segmentTree.query(1, 5)
print(summation)

segmentTree.update(2, 10)

summation = segmentTree.query(1, 5)
print(summation)

# Leetcode 307