from collections import defaultdict
from typing import List


class Solution:
    class TrieNode:
        def __init__(self, folder):
            self.folder = folder
            self.remove = False
            self.child = defaultdict(lambda: None)

    def trieInsert(self, node, path):
        cur = node
        for s in path:
            if s not in cur.child:
                cur.child[s] = self.TrieNode(s)
            cur = cur.child[s]

    def markRepeating(self, node, visited):
        subfolder = []
        for child_folder, child_node in node.child.items():
            subfolder.append(self.markRepeating(child_node, visited))

        key = ''.join(subfolder)
        if subfolder:
            if key in visited:
                visited[key].remove = True
                node.remove = True
            else:
                visited[key] = node
        return f"[{node.folder}{''.join(subfolder)}]"

    def savePath(self, node, curr_path, res):
        if node.remove:
            return

        curr_path.append(node.folder)
        res.append(curr_path.copy())
        for child_folder, child_node in node.child.items():
            self.savePath(child_node, curr_path, res)
        curr_path.pop()

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Step-1: Insert all paths in TRIE
        root = self.TrieNode("/")
        paths.sort()
        for path in paths:
            self.trieInsert(root, path)

        # Step-2: Mark repeating paths
        visited = {}
        self.markRepeating(root, visited)

        # Step-3: Save the path after deletion
        res = []
        curr_path = []
        for child_folder, child_node in root.child.items():
            self.savePath(child_node, curr_path, res)

        return res


s = Solution()
print(s.deleteDuplicateFolder(paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]))
print(s.deleteDuplicateFolder(
    paths=[["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]))
print(s.deleteDuplicateFolder(paths=[["a", "b"], ["c", "d"], ["c"], ["a"]]))
