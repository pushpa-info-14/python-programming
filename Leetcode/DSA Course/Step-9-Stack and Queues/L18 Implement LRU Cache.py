class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity
        self.mp = {}

    def delete(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_after_head(self, node: Node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.delete(node)
        self.insert_after_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.delete(node)
            self.insert_after_head(node)
        elif self.size < self.capacity:
            node = Node(key, value)
            self.mp[key] = node
            self.insert_after_head(node)
            self.size += 1
        else:
            delete_node = self.tail.prev
            self.delete(delete_node)
            self.mp.pop(delete_node.key)
            node = Node(key, value)
            self.mp[key] = node
            self.insert_after_head(node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
cache.put(4, 4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
