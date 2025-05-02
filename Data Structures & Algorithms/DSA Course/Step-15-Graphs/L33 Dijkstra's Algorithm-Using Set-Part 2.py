from typing import List


def shortestPath(src: int, graph: List[List[List[int]]]):
    n = len(graph)
    int_max = 10 ** 9
    distance = [int_max] * n
    st = [(0, src)]
    distance[src] = 0

    while st:
        dist, node = st.pop()
        for nei, w in graph[node]:
            if distance[nei] > dist + w:
                if distance[nei] != int_max:
                    if (distance[nei], nei) in st:
                        st.remove((distance[nei], nei))
                distance[nei] = dist + w
                st.append((dist + w, nei))

    return distance


"""
Dijkstra's algorithm does not work when there is a negative edge or cycle
"""

print(shortestPath(0, [
    [[1, 4], [2, 4]],
    [[0, 4], [2, 2]],
    [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
    [[2, 3], [5, 2]],
    [[2, 1], [5, 3]],
    [[2, 6], [3, 2], [4, 3]]
]))
