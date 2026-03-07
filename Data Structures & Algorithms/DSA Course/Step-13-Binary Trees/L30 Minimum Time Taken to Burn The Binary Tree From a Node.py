from collections import deque
from typing import List

from Common.TreeNode import TreeNode


class Solution:
    def minimumTimeToBurn(self, root: TreeNode, target: TreeNode) -> List[int]:
        parent = {}
        target_node = None
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    target_node = node
                if node.left:
                    q.append(node.left)
                    parent[node.left] = node
                if node.right:
                    q.append(node.right)
                    parent[node.right] = node

        q.append(target_node)
        visited = set()
        t = -1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
            t += 1
        return t


s = Solution()
tree = TreeNode.build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(s.minimumTimeToBurn(tree, tree.left))
