from collections import defaultdict
from typing import List, Optional

from Common.TreeNode import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen = {}
        has_parent = defaultdict(bool)

        for parent, child, is_left in descriptions:
            if parent not in seen:
                seen[parent] = TreeNode(parent)
            if child not in seen:
                seen[child] = TreeNode(child)
            if is_left:
                seen[parent].left = seen[child]
            else:
                seen[parent].right = seen[child]
            has_parent[child] = True

        for key in seen.keys():
            if not has_parent[key]:
                return seen[key]


s = Solution()
s.createBinaryTree(descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]).inorder_traversal()
s.createBinaryTree(descriptions=[[1, 2, 1], [2, 3, 0], [3, 4, 1]]).inorder_traversal()
