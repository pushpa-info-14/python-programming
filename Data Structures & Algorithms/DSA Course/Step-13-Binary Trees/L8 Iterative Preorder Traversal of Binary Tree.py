from Common.TreeNode import TreeNode


def preorder(root):
    res = []
    if root is None:
        return res

    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(preorder(tree))
