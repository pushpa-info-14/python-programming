from collections import defaultdict
from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indexes = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number and self.index_to_number[index] != number:
            previous_number = self.index_to_number[index]
            self.number_to_indexes[previous_number].remove(index)
            if not self.number_to_indexes[previous_number]:
                del self.number_to_indexes[previous_number]
        self.index_to_number[index] = number
        self.number_to_indexes[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_to_indexes and len(self.number_to_indexes[number]) > 0:
            return self.number_to_indexes[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
print(obj.find(10))
print(obj.change(2, 10))
print(obj.change(1, 10))
print(obj.change(3, 10))
print(obj.change(5, 10))
print(obj.find(10))
print(obj.change(1, 20))
print(obj.find(10))
