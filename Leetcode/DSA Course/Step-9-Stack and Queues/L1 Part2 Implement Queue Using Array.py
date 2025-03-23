class Queue:
    def __init__(self, n):
        self.max_size = n
        self.array = [0] * n
        self.cur_size = 0
        self.start = -1
        self.end = -1

    def push(self, x):
        if self.cur_size == self.max_size:
            print("Queue is full")
            return None
        if self.cur_size == 0:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.max_size
        self.array[self.end] = x
        self.cur_size += 1

    def pop(self):
        if self.cur_size == 0:
            print("Queue is empty")
            return None
        element = self.array[self.start]
        if self.cur_size == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.max_size
        self.cur_size -= 1
        return element

    def peek(self):
        if self.cur_size == 0:
            print("Queue is empty")
            return None
        return self.array[self.start]

    def size(self):
        return self.cur_size


queue = Queue(10)
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.size())
