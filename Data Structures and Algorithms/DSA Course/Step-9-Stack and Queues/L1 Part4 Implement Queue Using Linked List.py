from Leetcode.Common.ListNode import ListNode


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.cur_size = 0

    def push(self, x):
        temp = ListNode(x)
        if self.start is None:
            self.start = temp
            self.end = temp
        else:
            self.end.next = temp
            self.end = temp
        self.cur_size += 1

    def pop(self):
        if self.start is None:
            print("Queue is empty")
            return None
        temp = self.start
        self.start = self.start.next
        self.cur_size -= 1
        return temp.val

    def peek(self):
        if self.start is None:
            print("Queue is empty")
            return None
        return self.start.val

    def size(self):
        return self.cur_size


queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.size())
