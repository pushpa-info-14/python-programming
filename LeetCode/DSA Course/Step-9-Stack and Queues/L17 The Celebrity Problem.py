from typing import List


def find_celebrity(matrix: List[List[int]]) -> int:
    n = len(matrix)
    know_me = [0] * n
    i_know = [0] * n
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                know_me[j] += 1
                i_know[i] += 1

    for i in range(n):
        if know_me[i] == n - 1 and i_know[i] == 0:
            return i
    return -1


def find_celebrity2(matrix: List[List[int]]) -> int:
    n = len(matrix)
    top = 0
    bottom = n - 1

    while top < bottom:
        if matrix[top][bottom]:
            top += 1
        elif matrix[bottom][top]:
            bottom -= 1
        else:
            top += 1
            bottom -= 1
    if top != bottom: return -1
    for i in range(n):
        if i == top: continue
        if matrix[top][i] == 1 or matrix[i][top] == 0:
            return -1
    return top


print(find_celebrity([[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(find_celebrity2([[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
