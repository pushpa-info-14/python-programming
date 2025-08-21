from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        histogram = [0] * n
        count = 0

        for i in range(m):
            # update histogram for row i
            for j in range(n):
                histogram[j] = histogram[j] + 1 if mat[i][j] == 1 else 0

            # stack of tuples (height, index, prev_count); start with sentinel
            stack = [(-1, -1, 0)]
            for j in range(n):
                while stack and stack[-1][0] >= histogram[j]:
                    stack.pop()
                prev_h, prev_idx, prev_count = stack[-1]
                curr_count = histogram[j] * (j - prev_idx) + prev_count
                stack.append((histogram[j], j, curr_count))
                count += curr_count

        return count


s = Solution()
print(s.numSubmat(mat=[[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
print(s.numSubmat(mat=[[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]))
# 84, 85, 901
