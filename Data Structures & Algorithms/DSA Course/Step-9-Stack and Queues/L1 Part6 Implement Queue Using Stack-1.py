from collections import deque


class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x):
        while len(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2):
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def size(self):
        return len(self.s1)


queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.size())
