from Common.TreeNode import TreeNode


def preorder(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

preorder(tree)
