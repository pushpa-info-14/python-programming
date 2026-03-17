from Common.TreeNode import TreeNode


class Solution:
    def ceilInBST(self, root: TreeNode, val: int) -> int:
        res = -1
        cur = root
        while cur:
            if cur.val == val:
                return cur.val
            if val < cur.val:
                res = cur.val
                cur = cur.left
            else:
                cur = cur.right
        return res


# Smallest value greater than or equal to given value
s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
print(s.ceilInBST(tree, 2))
print(s.ceilInBST(tree, 8))
