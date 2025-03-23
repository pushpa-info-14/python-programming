class Stack:
    def __init__(self, n):
        self.array = [0] * n
        self.top = -1

    def push(self, x):
        self.top += 1
        self.array[self.top] = x

    def peek(self):
        if self.top == -1:
            print("empty")
            return None
        return self.array[self.top]

    def pop(self):
        if self.top == -1:
            print("empty")
            return None
        self.top -= 1
        return self.array[self.top + 1]

    def size(self):
        return self.top + 1


stack = Stack(10)
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.size())
