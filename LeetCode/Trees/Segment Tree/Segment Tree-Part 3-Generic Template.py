class Node:
    def __init__(self, val=0):
        self.val = val

    def merge(self, l, r):
        self.val = l.val + r.val


class Update:
    def __init__(self, val=0):
        self.val = val

    def combine(self, other_update):
        self.val += other_update.val

    def apply(self, node: Node, tl: int, tr: int):
        node.val += (tr - tl + 1) * self.val


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [Node() for _ in range(4 * size + 1)]
        self.isLazy = [False] * (4 * size + 1)
        self.pendingUpdates = [Update() for _ in range(4 * size + 1)]
        self.identityElement = Node()
        self.identityTransformation = Update()

    def _build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = Node(arr[tl])
            return

        tm = (tl + tr) // 2
        self._build(arr, 2 * v, tl, tm)
        self._build(arr, 2 * v + 1, tm + 1, tr)
        self.tree[v].merge(self.tree[2 * v], self.tree[2 * v + 1])

    def _query(self, v, tl, tr, l, r):
        if tr < l or tl > r:  # No overlap
            return self.identityElement
        if l <= tl and tr <= r:  # Full overlap
            return self.tree[v]

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        left_ans = self._query(2 * v, tl, tm, l, r)
        right_ans = self._query(2 * v + 1, tm + 1, tr, l, r)
        ans = Node()
        ans.merge(left_ans, right_ans)
        return ans

    def _pushDown(self, v, tl, tr):
        if not self.isLazy[v]:
            return
        self.isLazy[v] = False
        tm = (tl + tr) // 2
        self._apply(2 * v, tl, tm, self.pendingUpdates[v])
        self._apply(2 * v + 1, tm + 1, tr, self.pendingUpdates[v])
        self.pendingUpdates[v].val = self.identityTransformation.val

    def _apply(self, v: int, tl: int, tr: int, update: Update):
        if tl != tr:  # Leaf nodes can't be lazy
            self.isLazy[v] = True
            self.pendingUpdates[v].combine(update)
        update.apply(self.tree[v], tl, tr)

    def _update(self, v: int, tl: int, tr: int, l: int, r: int, update: Update):
        if l <= tl and tr <= r:  # Full overlap
            self._apply(v, tl, tr, update)
            return
        if r < tl or tr < l:  # No overlap
            return

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        self._update(2 * v, tl, tm, l, r, update)
        self._update(2 * v + 1, tm + 1, tr, l, r, update)
        self.tree[v].merge(self.tree[2 * v], self.tree[2 * v + 1])

    def build(self, arr):
        self._build(arr, 1, 0, self.size - 1)

    def query(self, l: int, r: int):
        return self._query(1, 0, self.size - 1, l, r)

    def update(self, l: int, r: int, update: Update):
        self._update(1, 0, self.size - 1, l, r, update)


nums = [1, 2, 1, 4, 2, 3, 1, 1]
n = len(nums)
segmentTree = SegmentTree(n)
segmentTree.build(nums)
print([segmentTree.query(i, i).val for i in range(n)])

summation = segmentTree.query(1, 5)
print(summation.val)

segmentTree.update(2, 2, Update(10))
summation = segmentTree.query(1, 5)
print(summation.val)
print([segmentTree.query(i, i).val for i in range(n)])

segmentTree.update(2, 7, Update(10))
print([segmentTree.query(i, i).val for i in range(n)])
segmentTree.update(2, 7, Update(20))
print([segmentTree.query(i, i).val for i in range(n)])
segmentTree.update(2, 7, Update(10))
print([segmentTree.query(i, i).val for i in range(n)])
segmentTree.update(2, 7, Update(20))
print([segmentTree.query(i, i).val for i in range(n)])
