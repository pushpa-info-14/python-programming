from Common.TreeNode import TreeNode


def getInorder(root):
    res = []
    cur = root
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                res.append(cur.val)
                cur = cur.right
    return res


def getPreorder(root):
    res = []
    cur = root
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if not prev.right:
                prev.right = cur
                res.append(cur.val)
                cur = cur.left
            else:
                prev.right = None
                cur = cur.right
    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(getInorder(tree))
print(getPreorder(tree))
