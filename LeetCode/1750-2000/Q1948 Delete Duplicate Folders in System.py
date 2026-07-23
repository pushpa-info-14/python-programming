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

    def deleteDuplicateFolder2(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {"#": "/"}
        for path in paths:
            c_node = tree
            for node in path:
                if node not in c_node:
                    c_node[node] = {"#": node}
                c_node = c_node[node]

        content_map = defaultdict(list)

        def mark(c_node, parent):
            if len(c_node) == 1:
                return c_node["#"]

            content = ""
            for child in sorted(c_node[k]["#"] for k in c_node if k != "#"):
                if child != "#":
                    content += mark(c_node[child], c_node)
            content_map[content].append((c_node["#"], parent))
            return f'{c_node["#"]}({content})'

        mark(tree, {})

        for v in content_map.values():
            if len(v) > 1:
                for node, parent in v:
                    del parent[node]

        remaining_paths = []

        def create_paths(c_node, c_path):
            c_path = c_path + [c_node["#"]]
            remaining_paths.append(c_path)

            for child in c_node:
                if child != "#":
                    create_paths(c_node[child], c_path)

        for k in tree:
            if k != "#":
                create_paths(tree[k], [])

        return remaining_paths


s = Solution()
print(s.deleteDuplicateFolder(paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]))
print(s.deleteDuplicateFolder(
    paths=[["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]))
print(s.deleteDuplicateFolder(paths=[["a", "b"], ["c", "d"], ["c"], ["a"]]))
print(s.deleteDuplicateFolder2(paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]))
print(s.deleteDuplicateFolder2(
    paths=[["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]))
print(s.deleteDuplicateFolder2(paths=[["a", "b"], ["c", "d"], ["c"], ["a"]]))
