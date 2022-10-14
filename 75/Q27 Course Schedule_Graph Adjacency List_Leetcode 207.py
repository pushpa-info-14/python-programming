"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want
to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
from typing import List


def can_finish(num_courses: int, prerequisites: List[list[int]]):
    # map each course to prerequisites list
    pre_map = {i:[] for i in range(num_courses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    # all courses along the current DFS path
    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        if not pre_map[crs]:
            return True

        visited.add(crs)
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
        visited.remove(crs)
        pre_map[crs] = []
        return True

    for crs in range(num_courses):
        if not dfs(crs):
            return False
    return True

    # 1 -> 2
    # 3 -> 4
    # Can be a disconnected graph


n = 6
prerequisites1 = [[0, 1], [3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
prerequisites2 = [[3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
print(can_finish(n, prerequisites1))
print(can_finish(n, prerequisites2))

