from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mx = 10 ** 5
        bit_len = mx.bit_length()

        # Is it possible to get a number from every row to get "0"
        # where the prefix is less than current
        def possible(index):
            prefix = current >> (index + 1)
            for r in range(m):
                found = False
                for c in range(n):
                    if (grid[r][c] >> (index + 1)) | prefix == prefix and grid[r][c] & (1 << index) == 0:
                        found = True
                        break
                if not found:
                    return False
            return True

        current = 0
        for i in range(bit_len - 1, -1, -1):
            if not possible(i):
                current |= (1 << i)
        return current


s = Solution()
print(s.minimumOR(grid=[[1, 5], [2, 4]]))
print(s.minimumOR(grid=[[3, 5], [6, 4]]))
print(s.minimumOR(grid=[[7, 9, 8]]))
