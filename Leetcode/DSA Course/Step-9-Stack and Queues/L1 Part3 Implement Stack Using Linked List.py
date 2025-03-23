from Leetcode.Common.ListNode import ListNode


class Stack:
    def __init__(self):
        self.top = None
        self.cur_size = 0

    def push(self, x):
        temp = ListNode(x)
        temp.next = self.top
        self.top = temp
        self.cur_size += 1

    def pop(self):
        temp = self.top
        self.top = self.top.next
        self.cur_size -= 1
        return temp.val

    def peek(self):
        return self.top.val

    def size(self):
        return self.cur_size


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.size())
