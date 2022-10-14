import heapq

def kth_largest1(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

# T(n,k) = (k - 1) * 2n + n = 2kn - n = O(kn)
# S(n,k) = O(1)


# Using sorted array
def kth_largest2(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n - k]

# T(n,k) = O(nlogn) + O(1) = O(nlogn)
# S(n,k) = O(1)


def kth_largest3(arr, k):
    # Min heap is implemented. We need max heap.
    arr = [-elem for elem in arr]  # n
    heapq.heapify(arr)  # n
    for i in range(k-1):  # k - 1
        heapq.heappop(arr)  # logn
    return -heapq.heappop(arr)  # logn

# T(n,k) = 2n + (k-1)logn + logn
# T(n,k) = 2n + klogn = O(n + klogn)
# S(n,k) = O(n)


arr_test1 = [4, 2, 9, 7, 5, 6, 7, 1, 3]
arr_test2 = [4, 2, 9, 7, 5, 6, 7, 1, 3]
arr_test3 = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k_test = 4
print(kth_largest1(arr_test1, k_test))
print(kth_largest2(arr_test2, k_test))
print(kth_largest3(arr_test3, k_test))
