"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node
with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an
adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set
of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference
 to the cloned graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with
    val = 1, and it does not have any neighbors.

Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.
"""
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def create_graph(adjacency_list: List[List[int]]):
    nodes = {}

    for index, neighbors in enumerate(adjacency_list):
        node_val = index + 1
        if node_val not in nodes:
            nodes[node_val] = Node(node_val)

        for neighbor in neighbors:
            if neighbor not in nodes:
                nodes[neighbor] = Node(neighbor)
            nodes[node_val].neighbors.append(nodes[neighbor])

    return nodes[1]


def get_graph_adjacency_list(node: Node):
    adjacency_dict = {}
    adjacency_list = []
    visited = []

    def dfs(node: Node):
        if node in visited:
            return
        else:
            visited.append(node)
            if node.val not in adjacency_dict:
                adjacency_dict[node.val] = []
            if not node.neighbors:
                return
            for neighbor in node.neighbors:
                adjacency_dict[node.val].append(neighbor.val)
                dfs(neighbor)
    dfs(node)
    t = len(adjacency_dict.keys())
    for i in range(1, t+1):
        adjacency_list.append(adjacency_dict[i])
    return adjacency_list


def clone_graph(node):
    old_to_new = {}

    def dfs(node: Node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node) if node else None


adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
graph = create_graph(adj_list)
print(get_graph_adjacency_list(graph))
print(get_graph_adjacency_list(clone_graph(graph)))

