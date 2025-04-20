class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, x):
        if len(self.stack) == 0:
            self.minimum = x
            self.stack.append(x)
        else:
            if x > self.minimum:
                self.stack.append(x)
            else:
                self.stack.append(2 * x - self.minimum)
                self.minimum = x

    def get_min(self):
        return self.minimum

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        x = self.stack.pop()
        if x < self.minimum:
            temp = self.minimum
            self.minimum = 2 * self.minimum - x
            return temp
        else:
            return x

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        x = self.stack[-1]
        if x > self.minimum:
            return x
        else:
            return self.minimum


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
