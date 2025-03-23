from collections import deque


class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        s = len(self.q)
        self.q.append(x)

        for i in range(s):
            self.q.append(self.q[0])
            self.q.popleft()

    def pop(self):
        return self.q.popleft()

    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.size())
