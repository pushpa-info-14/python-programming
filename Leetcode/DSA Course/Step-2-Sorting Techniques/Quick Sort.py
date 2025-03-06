"""
Divide and Conquer algorithm
    -Breaks down problems into multiple sub-problems recursively until
     they become simple to solve
    -Solutions are combined to solve original problem

Running time
    -O(n²) worst case
    -O(n*log(n)) best and average case

General Principle
    1. Choose pivot element
    2. Stores elements less than pivot in left subarray
    3. Stores elements greater than pivot in right subarray
    4. Call quicksort recursively on left subarray
    5. Call quicksort recursively on right subarray

"""


def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]

    while i < j:
        # Find the first element greater than the pivot
        while i < high and arr[i] <= pivot:
            i += 1
        # Find the first element smaller than the pivot
        while j > low and arr[j] > pivot:
            j -= 1
        # Swap smaller element with greater element
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]

    return j


def quickSort(arr, low, high):
    if low < high:
        partition_pos = partition(arr, low, high)
        quickSort(arr, low, partition_pos - 1)
        quickSort(arr, partition_pos + 1, high)


nums = [2, 1, 8, 6, 5, 9, 7, 3, 4]
quickSort(nums, 0, len(nums) - 1)
print(nums)
