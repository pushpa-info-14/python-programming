from typing import Optional

from Common.TreeNode import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            cur = node.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


tree = TreeNode.build([7, 3, 15, None, None, 9, 20])
s = BSTIterator(tree)
print(s.next())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
