from collections import defaultdict
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        def dfs(node):
            if visited[node] == 1:  # Cycle found
                return True

            if visited[node] == 0:  # Visiting for the 1st time
                visited[node] = 1
                for nei in adj[node]:
                    if dfs(nei):
                        return True

                    # Iterate for each color for the current nei and update max_len for each color at current node
                    for color in range(26):
                        longest[color][node] = max(longest[color][node], longest[color][nei])

                longest[ord(colors[node]) - ord('a')][node] += 1
                visited[node] = 2

            return False

        n = len(colors)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        longest = [[0] * n for _ in range(26)]
        """
            longest: Table to store the count of each color from a given node
            longest[i][j]=X: There are 'X' number of 'i' color nodes from current node 'j'
        """
        res = 0
        visited = [0] * n
        """
            3-color method is used to detect cycle in directed graph.
            0: Unvisited
            1: Visited & Processing
            2: Visited & Processed
        """
        # Perform DFS from each node and maximize color length
        for i in range(n):
            if dfs(i):
                return -1
            res = max(res, longest[ord(colors[i]) - ord('a')][i])
        return res


s = Solution()
print(s.largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
print(s.largestPathValue(colors="a", edges=[[0, 0]]))
print(s.largestPathValue(colors="hhqhuqhqff",
                         edges=[[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [6, 7], [7, 8], [3, 8], [5, 8],
                                [8, 9], [3, 9], [6, 9]]))
print(s.largestPathValue(colors="bbbhb", edges=[[0, 2], [3, 0], [1, 3], [4, 1]]))
