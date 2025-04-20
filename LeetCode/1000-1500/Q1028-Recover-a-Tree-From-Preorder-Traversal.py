from typing import Optional

from Leetcode.Common.TreeNode import TreeNode


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        elements = []
        l = 0
        for i in range(n):
            if i < l:
                continue
            # Level
            level = 0
            while l < n and traversal[l] == "-":
                level += 1
                l += 1
            # Value
            val = ""
            while l < n and traversal[l] != "-":
                val += traversal[l]
                l += 1

            elements.append([level, int(val)])
        print(elements)

        stack = []
        root = None
        for level, val in elements:
            node = TreeNode(val)
            if len(stack) == 0:
                root = node
            else:
                while level - 1 != stack[-1][0]:
                    stack.pop()
                if stack[-1][1].left is None:
                    stack[-1][1].left = node
                else:
                    stack[-1][1].right = node
            stack.append([level, node])
        return root


s = Solution()

print(s.recoverFromPreorder("1-2--3--4-5--6--7").preorder_traversal())
print(s.recoverFromPreorder("1-2--3---4-5--6---7").preorder_traversal())
print(s.recoverFromPreorder("1-401--349---90--88").preorder_traversal())
print(s.recoverFromPreorder("3").preorder_traversal())
