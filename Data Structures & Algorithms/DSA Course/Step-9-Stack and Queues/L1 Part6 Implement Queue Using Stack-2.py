from collections import deque


class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if len(self.s2):
            return self.s2.pop()
        else:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    def peek(self):
        if len(self.s2):
            return self.s2[-1]
        else:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2[-1]

    def size(self):
        return len(self.s1) + len(self.s2)


queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.size())
