"""
Divide and Conquer algorithm
    -Breaks down problems into multiple sub-problems recursively until
     they become simple to solve
    -Solutions are combined to solve original problem

Running time
    -O(n²) worst case
    -O(n*log(n)) best and average case

General Principle
    1. Choose pivot element (Usually last or random)
    2. Stores elements less than pivot in left subarray
    3. Stores elements greater than pivot in right subarray
    4. Call quicksort recursively on left subarray
    5. Call quicksort recursively on right subarray

"""


def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        # Finds smaller elements than the pivot
        while i < right and arr[i] < pivot:
            i += 1
        # Finds higher elements than the pivot
        while j > left and arr[j] >= pivot:
            j -= 1
        # Swap smaller element with higher element
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [2, 1, 8, 6, 5, 7, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
