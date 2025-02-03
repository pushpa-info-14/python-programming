import heapq


def heap_sort(nums):
    q = []
    for num in nums:
        heapq.heappush(q, num)

    return [heapq.heappop(q) for _ in range(len(nums))]


print(heap_sort([9, 8, 4, 5, 6, 7, 3, 2, 1]))
