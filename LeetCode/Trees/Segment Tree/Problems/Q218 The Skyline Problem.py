from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, l, r, h):
        if start > r or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] = max(self.tree[node], h)
            return
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, h)
        self.update(2 * node + 1, mid + 1, end, l, r, h)

    def query(self, node, start, end, idx):
        if start == end:
            return self.tree[node]
        mid = (start + end) // 2
        if idx <= mid:
            return max(self.tree[node], self.query(2 * node, start, mid, idx))
        else:
            return max(self.tree[node], self.query(2 * node + 1, mid + 1, end, idx))


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = sorted(set([x for b in buildings for x in (b[0], b[1])]))
        index = {x: i for i, x in enumerate(points)}

        tree = SegmentTree(len(points))
        for L, R, H in buildings:
            tree.update(1, 0, len(points) - 1, index[L], index[R] - 1, H)

        result, prev_height = [], 0
        for x in points:
            height = tree.query(1, 0, len(points) - 1, index[x])
            if height != prev_height:
                result.append([x, height])
                prev_height = height

        return result


s = Solution()
print(s.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
print(s.getSkyline(buildings=[[0, 2147483647, 2147483647]]))
