def parent(i):
    return i // 2


def left_child(i):
    return i * 2


def right_child(i):
    return i * 2 + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heappush(arr, val):
    arr.append(val)
    heapify_up(arr, len(arr) - 1)


def heappop(arr):
    val = arr[0]
    swap(arr, 0, len(arr) - 1)
    del arr[-1]
    heapify_down(arr, 0)
    return val


def heapify_up(arr, i):
    if i == 0:
        return
    p = parent(i)

    if arr[p] < arr[i]:
        swap(arr, p, i)
        heapify_up(arr, p)


def heapify_down(arr, i):
    n = len(arr)
    l = left_child(i)
    r = right_child(i)

    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        swap(arr, i, largest)
        heapify_down(arr, largest)


nums1 = [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 10]

print(nums1)
# 0 to n/2 in reverse order
for index in reversed(range(len(nums1) // 2)):
    heapify_down(nums1, index)

print([heappop(nums1) for _ in range(len(nums1))])
print(nums1)

nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums2)
heap = []
for num in nums2:
    heappush(heap, num)
print([heappop(heap) for _ in range(len(nums2))])
