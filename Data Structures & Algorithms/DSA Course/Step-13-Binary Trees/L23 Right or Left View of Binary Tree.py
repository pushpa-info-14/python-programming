from Common.BinaryTreeNode import BinaryTreeNode


def leftView(root):
    res = []

    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.data)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return res


def rightView(root):
    res = []

    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.data)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return res


# Level order traversal may use more memory
tree = BinaryTreeNode.build(
    [1, 2, 3, 4, 5, None, 6, None, 7, None, None, 8, None, 9, None, None, 11, 10, None, None, None, None, None])
print(leftView(tree))
tree = BinaryTreeNode.build(
    [2, 35, 10, 2, 3, 5, 2])
print(leftView(tree))
print(rightView(tree))
