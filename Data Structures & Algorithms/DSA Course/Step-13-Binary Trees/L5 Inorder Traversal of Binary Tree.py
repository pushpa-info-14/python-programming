from Common.TreeNode import TreeNode


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


root = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

inorder(root)