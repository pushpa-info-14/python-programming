from Common.TreeNode import TreeNode


class Solution:
    def floorInBST(self, root: TreeNode, val: int) -> int:
        res = -1
        cur = root
        while cur:
            if cur.val == val:
                return cur.val
            if val < cur.val:
                cur = cur.left
            else:
                res = cur.val
                cur = cur.right
        return res


# Greatest value less than or equal to given value
s = Solution()
tree = TreeNode.build([10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9])
print(s.floorInBST(tree, 2))
print(s.floorInBST(tree, 8))
