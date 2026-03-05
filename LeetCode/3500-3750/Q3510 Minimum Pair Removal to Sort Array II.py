import heapq
from typing import List


class Node:
    def __init__(self, value, left):
        self.value = value
        self.left = left # Original index
        self.prev = None
        self.next = None


class Item:
    def __init__(self, first, second, cost):
        self.first = first
        self.second = second
        self.cost = cost # The sum of the pair

    def __lt__(self, other):
        # Sort by cost (sum), then by index (leftmost)
        if self.cost == other.cost:
            return self.first.left < other.first.left
        return self.cost < other.cost


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        decrease_count = 0
        count = 0

        for i in range(1, len(nums)):
            new_node = Node(nums[i], i)
            current.next = new_node
            new_node.prev = current
            heapq.heappush(pq, Item(current, new_node, current.value + new_node.value))

            if nums[i - 1] > nums[i]:
                decrease_count += 1

            current = new_node

        while decrease_count > 0:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if merged[first.left] or merged[second.left] or first.value + second.value != cost:
                continue
            count += 1

            if first.value > second.value:
                decrease_count -= 1

            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if next_node:
                next_node.prev = first

            if prev_node:
                if first.value < prev_node.value <= cost:
                    decrease_count -= 1
                elif first.value >= prev_node.value > cost:
                    decrease_count += 1
                heapq.heappush(pq, Item(prev_node, first, prev_node.value + cost))

            if next_node:
                if second.value > next_node.value >= cost:
                    decrease_count -= 1
                elif second.value <= next_node.value < cost:
                    decrease_count += 1
                heapq.heappush(pq, Item(first, next_node, cost + next_node.value))

            first.value = cost
            merged[second.left] = True

        return count


s = Solution()
print(s.minimumPairRemoval(nums=[5, 2, 3, 1]))
print(s.minimumPairRemoval(nums=[1, 2, 2]))
