"""
You are given a starting position for a rat which is stuck in a maze at an initial point (0, 0)
(the maze can be thought of as a 2-dimensional plane). The maze would be given in the form of a
square matrix of order 'N' * 'N' where the cells with value 0 represent the maze’s blocked locations
while value 1 is the open/available path that the rat can take to reach its destination. The rat's
destination is at ('N' - 1, 'N' - 1). Your task is to find all the possible paths that the rat can
take to reach from source to destination in the maze. The possible directions that it can take to
move in the maze are 'U'(up) i.e. (x, y - 1) , 'D'(down) i.e. (x, y + 1) , 'L' (left) i.e. (x - 1, y),
'R' (right) i.e. (x + 1, y).

Note:
Here, sorted paths mean that the expected output should be in alphabetical order.
For Example:
Given a square matrix of size 4*4 (i.e. here 'N' = 4):
1 0 0 0
1 1 0 0
1 1 0 0
0 1 1 1
Expected Output:
DDRDRR DRDDRR
i.e. Path-1: DDRDRR and Path-2: DRDDRR

The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR
when printed in sorted order, we get DDRDRR DRDDRR.
"""


def searchMaze(arr, n):
    res = []
    visited = [[0] * n for _ in range(n)]
    path = []
    directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]  # D L R U
    moves = ["D", "L", "R", "U"]

    def dfs(r, c):
        if r == n - 1 and c == n - 1:
            res.append("".join(path))
            return

        for i in range(4):
            nr = r + directions[i][0]
            nc = c + directions[i][1]
            if nr < 0 or nc < 0 or nr == n or nc == n or arr[nr][nc] == 0 or visited[nr][nc]:
                continue
            path.append(moves[i])
            visited[nr][nc] = 1
            dfs(nr, nc)
            path.pop()
            visited[nr][nc] = 0

    if arr[0][0] == 1:
        visited[0][0] = 1
        dfs(0, 0)
    return res


print(searchMaze([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]], 4))
print(searchMaze([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 3))
