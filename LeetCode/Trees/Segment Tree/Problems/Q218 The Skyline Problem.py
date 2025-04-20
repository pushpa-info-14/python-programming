from typing import List

from typing import List

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size + 1)
        self.isLazy = [False] * (4 * size + 1)
        self.pendingUpdates = [0] * (4 * size + 1)

    def _query(self, v, tl, tr, l, r):
        if tr < l or tl > r:  # No overlap
            return 0
        if l <= tl and tr <= r:  # Full overlap
            return self.tree[v]

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        left_ans = self._query(2 * v, tl, tm, l, r)
        right_ans = self._query(2 * v + 1, tm + 1, tr, l, r)
        return max(left_ans , right_ans)

    def _update(self, v, tl, tr, l, r, val):
        if r < tl or tr < l:  # No overlap
            return
        if l <= tl and tr <= r:  # Full overlap
            self._apply(v, tl, tr, val)
            return

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        self._update(2 * v, tl, tm, l, r, val)
        self._update(2 * v + 1, tm + 1, tr, l, r, val)
        self.tree[v] = max(self.tree[2 * v] , self.tree[2 * v + 1])

    def _pushDown(self, v, tl, tr):
        if not self.isLazy[v]:
            return
        self.isLazy[v] = False
        tm = (tl + tr) // 2
        self._apply(2 * v, tl, tm, self.pendingUpdates[v])
        self._apply(2 * v + 1, tm + 1, tr, self.pendingUpdates[v])
        self.pendingUpdates[v] = 0

    def _apply(self, v, tl, tr, val):
        if tl != tr:  # Leaf nodes can't be lazy
            self.isLazy[v] = True
            self.pendingUpdates[v] = max(self.pendingUpdates[v], val)
        self.tree[v] = max(self.tree[v],  val)

    def query(self, l, r):
        return self._query(1, 0, self.size - 1, l, r)

    def update(self, l, r, val):
        self._update(1, 0, self.size - 1, l, r, val)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = sorted(set([x for b in buildings for x in (b[0], b[1])]))
        index = {x: i for i, x in enumerate(points)}

        tree = SegmentTree(len(points))
        for L, R, H in buildings:
            tree.update(index[L], index[R] - 1, H)

        result, prev_height = [], 0
        for x in points:
            height = tree.query(index[x], index[x])
            if height != prev_height:
                result.append([x, height])
                prev_height = height

        return result


s = Solution()
print(s.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
print(s.getSkyline(buildings=[[0, 2147483647, 2147483647]]))
