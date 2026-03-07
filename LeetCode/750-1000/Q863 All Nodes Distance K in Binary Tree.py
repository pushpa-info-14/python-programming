from collections import deque
from typing import List

from Common.TreeNode import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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

        res = []
        q.append(target_node)
        visited = set()
        distance = 0
        while q:
            if distance == k:
                break
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
            distance += 1

        while q:
            node = q.popleft()
            res.append(node.val)
        return res


s = Solution()
tree = TreeNode.build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(s.distanceK(tree, tree.left, 2))
