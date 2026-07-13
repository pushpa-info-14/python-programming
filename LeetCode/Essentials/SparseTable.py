import math


class SparseTable:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.LOG = math.floor(math.log2(self.n)) + 1

        # st[i][j] = minimum in range [i, i + 2^j - 1]
        self.st = [[0] * self.LOG for _ in range(self.n)]

        # Initialize for intervals of length 1
        for i in range(self.n):
            self.st[i][0] = arr[i]

        # Build sparse table
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) <= self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, left, right):
        length = right - left + 1
        k = length.bit_length() - 1

        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])


# Example
arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]

st = SparseTable(arr)

print(st.query(0, 4))  # 0
print(st.query(4, 7))  # 3
print(st.query(7, 8))  # 12
print(st.query(0, 8))  # 0
