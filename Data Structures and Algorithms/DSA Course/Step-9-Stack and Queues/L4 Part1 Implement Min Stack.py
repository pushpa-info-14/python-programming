import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = math.inf

    def push(self, x):
        self.minimum = min(self.minimum, x)
        self.stack.append((x, self.minimum))

    def get_min(self):
        return self.minimum

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        el = self.stack.pop()[0]
        self.minimum = self.stack[-1][1]
        return el

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        return self.stack[-1][0]


stack = MinStack()
stack.push(12)
stack.push(15)
stack.push(10)
print(stack.get_min())
print(stack.pop())
print(stack.get_min())
print(stack.peek())
stack.push(10)
print(stack.peek())
