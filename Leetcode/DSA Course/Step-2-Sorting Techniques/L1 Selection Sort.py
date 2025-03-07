def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):  # 0 -> n - 2
        mini = i
        for j in range(i, n): # 0 -> n - 1
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


nums = [13, 46, 24, 52, 20, 9]
print(nums)
selectionSort(nums)
print(nums)

# O(n²) All cases
