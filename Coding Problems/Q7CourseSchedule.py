"""
Given an integer n representing the number of courses (courses are labeled from 0 to n - 1),
and an array prerequisites where prerequisites[i] = [A,B] means that you first need to take
the course B before takin the course A. Determine if it's possible to finish all the courses
"""
from collections import deque


def dfs(graph, vertex, path, order, visited):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)
    order.append(vertex)
    return True


def course_schedule1(n, prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
    return True
# T(V,E) = O(|V|+|E|) = O(n+m)
# S(V,E) = 4|V|+|E|)
# S(V,E) = 4n + m = O(n+m)


def course_schedule2(n, prerequisites):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n


n_test = 6
prerequisites_test1 = [[0, 1], [3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
prerequisites_test2 = [[3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
print(course_schedule1(n_test, prerequisites_test1))
print(course_schedule1(n_test, prerequisites_test2))
print(course_schedule2(n_test, prerequisites_test1))
print(course_schedule2(n_test, prerequisites_test2))
