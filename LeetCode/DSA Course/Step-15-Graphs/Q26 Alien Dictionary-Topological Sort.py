from collections import deque
from typing import List


def topologicalSort(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    in_degree = [0] * n
    for i in range(n):
        for nei in graph[i]:
            in_degree[nei] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)
    return res


def getAlienLanguage(dictionary: List[str], k: int) -> str:
    adj = [[] for _ in range(k)]
    for i in range(len(dictionary) - 1):
        s1 = dictionary[i]
        s2 = dictionary[i + 1]
        l = min(len(s1), len(s2))
        for j in range(l):
            if s1[j] != s2[j]:
                adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                break
    topo = topologicalSort(adj)
    res = []
    for i in topo:
        res.append(chr(i + ord('a')))
    return "".join(res)


"""
# Not possible when
    Wrong order
    [ abcd
      abc ]

    Cycle 
    [ abc
      bat
      ade ]
"""

print(getAlienLanguage(["baa", "abcd", "abca", "cab", "cad"], 5))
print(getAlienLanguage(["a", "aa", "aaa"], 1))
print(getAlienLanguage(["caa", "aaa", "aab"], 3))
print(getAlienLanguage(["bbbc", "bba", "aaaaac"], 3))
