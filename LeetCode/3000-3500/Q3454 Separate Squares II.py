import bisect
from typing import List


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, start, end, val, l, r, node):
        if self.xs[r + 1] <= start or self.xs[l] >= end:
            return
        if start <= self.xs[l] and self.xs[r + 1] <= end:
            self.count[node] += val
        else:
            mid = (l + r) // 2
            self.update(start, end, val, l, mid, node * 2 + 1)
            self.update(start, end, val, mid + 1, r, node * 2 + 2)

        if self.count[node] > 0:
            self.covered[node] = self.xs[r + 1] - self.xs[l]
        else:
            if l == r:
                self.covered[node] = 0
            else:
                self.covered[node] = self.covered[node * 2 + 1] + self.covered[node * 2 + 2]

    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.update([x, x + l])
        xs = sorted(xs_set)

        st = SegmentTree(xs)
        events.sort()

        prefix_sum = []
        widths = []
        total_area = 0.0
        prev_y = events[0][0]

        # Scan: calculate total area and record intermediate states
        for y, delta, xl, xr in events:
            length = st.query()
            total_area += length * (y - prev_y)
            st.update(xl, xr, delta, 0, st.n - 1, 0)
            # record prefix sums and widths
            prefix_sum.append(total_area)
            widths.append(st.query())
            prev_y = y

        # Calculate the target area (half rounded up)
        target = (total_area + 1) // 2
        # Find the first position greater than or equal to target using binary search
        i = bisect.bisect_left(prefix_sum, target) - 1
        # Get the corresponding area, width, and height
        area = prefix_sum[i]
        width = widths[i]
        height = events[i][0]

        return height + (total_area - area * 2) / (width * 2.0)


s = Solution()
print(s.separateSquares(squares=[[0, 0, 1], [2, 2, 1]]))
print(s.separateSquares(squares=[[0, 0, 2], [1, 1, 1]]))
print(s.separateSquares(squares=[[23, 29, 3], [28, 29, 4]]))
