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


def heapify_down(arr, i, size=0):
    n = len(arr) if size == 0 else size
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
        heapify_down(arr, largest, size)


def heap_sort(arr):
    for i in reversed(range(len(arr) // 2)):
        heapify_down(arr, i)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i) # Swap heap root with last element
        heapify_down(arr, 0, i) # Heapify root with heap size = i


data = [1, 2, 7, 4, 5, 6, 3, 8, 10, 9]
print(data)
heap_sort(data)
print(data)
