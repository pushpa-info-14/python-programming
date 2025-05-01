def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


nums = [13, 46, 24, 52, 20, 9]
print(nums)
insertionSort(nums)
print(nums)

nums = [1, 2, 3, 4, 5, 6]
print(nums)
insertionSort(nums)
print(nums)

# O(n²) Worst case and average case
# O(n) Best case
