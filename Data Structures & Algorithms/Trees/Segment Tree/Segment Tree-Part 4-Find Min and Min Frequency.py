import math


class Node:
    def __init__(self, val=math.inf):
        self.val = val
        self.count = 1 if val != math.inf else 0

    def merge(self, l, r):
        self.val = min(l.val, r.val)
        self.count = 0
        if self.val == l.val: self.count += l.count
        if self.val == r.val: self.count += r.count


class Update:
    def __init__(self, val=0):
        self.val = val

    def combine(self, other_update):
        self.val = other_update.val

    def apply(self, node: Node, tl: int, tr: int):
        node.val = self.val
        node.count = tr - tl + 1


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


# Find min & freq of min in a range
nums = [1, 2, 1, 4, 2, 3, 1, 1]
n = len(nums)
segmentTree = SegmentTree(n)
segmentTree.build(nums)
print([segmentTree.query(i, i).val for i in range(n)])

minimum = segmentTree.query(1, 5).val
freq = segmentTree.query(1, 5).count
print(minimum, freq)

segmentTree.update(2, 2, Update(10))
minimum = segmentTree.query(1, 5).val
freq = segmentTree.query(1, 5).count
print(minimum, freq)
print([segmentTree.query(i, i).val for i in range(n)])

segmentTree.update(2, 2, Update(1))
segmentTree.update(3, 4, Update(1))
minimum = segmentTree.query(2, 5).val
freq = segmentTree.query(2, 5).count
print(minimum, freq)
print([segmentTree.query(i, i).val for i in range(n)])

"""
P1: Find min & freq of min in a range
P2: Range sum query - covered
P3: Range min query
P4: Add to the range [l, r] 
    Find the value at index i
P5: Set the value v in range [l, r] by the operation ai= max(ai, v)
    Find max value in range [l, r]
P6: Range assign update on the segment [l, r] with the value v (0 <= v <= 1e9)
    Range sum query [l, r]
P7: Add v to the segment [l, r]
    Find min on the segment [l, r]
P8: Multiply all the elements in range [l, r] by number v
    Find the sum of elements in the range [l, r] 
P9: Apply the operation ai = (ai | v) (bitwise OR) to all the elements in the range [l, r]
    Find the bitwise AND of all the elements in the range [l, r]
    
https://cp-algorithms.com/data_structures/segment_tree.html#practice-problems
"""

# LeetCode 307
# LeetCode 315, 3161
