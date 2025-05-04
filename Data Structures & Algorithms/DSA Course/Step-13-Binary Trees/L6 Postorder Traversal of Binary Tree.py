from Common.TreeNode import TreeNode


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

postorder(tree)