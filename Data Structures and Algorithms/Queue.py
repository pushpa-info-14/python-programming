from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


queue = Queue()

queue.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 Apr, 11:01 AM',
    'price': 131.10
})
queue.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 Apr, 11:02 AM',
    'price': 132
})
queue.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 Apr, 11:03 AM',
    'price': 135
})

print(queue.buffer)
print(queue.dequeue())
print(queue.buffer)
