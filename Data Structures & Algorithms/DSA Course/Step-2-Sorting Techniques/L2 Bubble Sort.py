def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


nums = [13, 46, 24, 52, 20, 9]
print(nums)
bubbleSort(nums)
print(nums)

nums = [1, 2, 3, 4, 5, 6]
print(nums)
bubbleSort(nums)
print(nums)

# O(n²) Worst case and average case
# O(n) Best case