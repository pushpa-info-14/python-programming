from Common.TreeNode import TreeNode


class Solution:
    def insertInBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val <= cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root


s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
s.insertInBST(tree, 12).preorder_traversal()
s.insertInBST(tree, 8).preorder_traversal()
