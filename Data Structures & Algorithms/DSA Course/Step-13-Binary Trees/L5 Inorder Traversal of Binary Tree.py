from Common.TreeNode import TreeNode


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

inorder(tree)