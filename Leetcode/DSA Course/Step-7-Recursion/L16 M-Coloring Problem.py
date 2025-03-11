"""
M-Coloring Problem

Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at
Most M colors such that no two adjacent vertices of the graph are colored with the same color. Here
coloring of a graph means the assignment of colors to all vertices.

https://www.naukri.com/code360/problems/m-coloring-problem_981273?leftPanelTabValue=PROBLEM
"""
from typing import List


def graphColoring(mat: List[List[int]], m: int) -> str:
    n = len(mat)
    colors = [0 for _ in range(n)]

    def isValid(node, color):
        for i in range(n):
            if i != node and mat[node][i] == 1 and colors[i] == color:
                return False
        return True

    def solve(node):
        if node == n:
            return True
        for color in range(1, m + 1):
            if isValid(node, color):
                colors[node] = color
                if solve(node + 1):
                    return True
                colors[node] = 0
        return False

    res = solve(0)
    return "YES" if res else "NO"


print(graphColoring([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 2))
print(graphColoring([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 1))
