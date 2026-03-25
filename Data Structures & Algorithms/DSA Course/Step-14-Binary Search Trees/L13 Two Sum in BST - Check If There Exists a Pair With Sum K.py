from typing import Optional

from Common.TreeNode import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode], reverse=False):
        self.reverse = reverse
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            if not self.reverse:
                cur = cur.left
            else:
                cur = cur.right

    def next(self) -> int:
        node = self.stack.pop()
        if not self.reverse:
            cur = node.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        else:
            cur = node.left
            while cur:
                self.stack.append(cur)
                cur = cur.right
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)
        i = l.next()
        j = r.next()
        while i < j:
            cur = i + j
            if cur < k:
                i = l.next()
            elif cur > k:
                j = r.next()
            else:
                return True
        return False


s = Solution()
tree = TreeNode.build([7, 3, 15, None, None, 9, 20])
print(s.findTarget(tree, 35))
print(s.findTarget(tree, 18))
print(s.findTarget(tree, 19))
