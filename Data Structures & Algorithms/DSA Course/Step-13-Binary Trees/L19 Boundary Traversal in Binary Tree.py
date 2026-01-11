from Common.TreeNode import TreeNode


def traverseBoundary(root):
    res = []

    def is_leaf(node):
        if node and not node.left and not node.right:
            return True
        return False

    def add_left_boundary(node):
        cur = node.left
        while cur:
            if not is_leaf(cur):
                res.append(cur.val)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right

    def add_right_boundary(node):
        cur = node.right
        temp = []
        while cur:
            if not is_leaf(cur):
                temp.append(cur.val)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        res.extend(temp[::-1])

    def add_leaf_nodes(node):
        if is_leaf(node):
            res.append(node.val)
            return
        if node.left:
            add_leaf_nodes(node.left)
        if node.right:
            add_leaf_nodes(node.right)

    if not root:
        return res
    if not is_leaf(root):
        res.append(root.val)
    add_left_boundary(root)
    add_leaf_nodes(root)
    add_right_boundary(root)

    return res


"""
Left boundary excluding leaf
Leaf nodes
Right boundary excluding leaf
"""
tree = TreeNode.build([10, 5, 20, 3, 8, 18, 25, None, None, 7])
print(traverseBoundary(tree))
tree = TreeNode.build(
    [100, 50, 150, 25, 75, 140, 200, None, 30, 70, 80, None, None, None, None, None, 35, None, None, None, None, None,
     None])
print(traverseBoundary(tree))
tree = TreeNode.build(
    [28, None, 4, 42, 40, 39, 2, 24, 41, None, None, None, None, None, 17, 15, 37, 45, 18, None, 33, 43, 35, None, None,
     23, None, None, None, None, None, None, 30, 12, None, None, None, None, 47, 7, None, None, 32, None, None])
print(traverseBoundary(tree))
