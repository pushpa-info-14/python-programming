class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def query(self, index):
        index += 1
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= (index & -index)
        return ans

    def update(self, index, val):
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += (index & -index)


nums = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(nums)
fenwick = FenwickTree(n)

for i in range(n):
    fenwick.update(i, nums[i])

# Range query
print(fenwick.query(7) - fenwick.query(0))
print(fenwick.query(7) - fenwick.query(6))
print(fenwick.query(7) - fenwick.query(5))

# Point update
fenwick.update(7, -nums[7])  # Firstly make it back to 0
nums[7] = 0  # Update your original input array
fenwick.update(7, nums[7])  # Update the bit array

# Range query
print(fenwick.query(7) - fenwick.query(0))
print(fenwick.query(7) - fenwick.query(6))
print(fenwick.query(7) - fenwick.query(5))

# LeetCode 315 Count of Smaller Numbers After Self
