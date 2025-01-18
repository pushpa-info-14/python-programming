import heapq

heap = []
heapq.heappush(heap,(1,2,3))
heapq.heappush(heap,(2,1,3))
heapq.heappush(heap,(2,0,3))

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))