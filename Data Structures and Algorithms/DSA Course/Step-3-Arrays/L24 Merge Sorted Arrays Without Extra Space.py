def mergeArraysBrute(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    temp = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            temp.append(nums1[i])
            i += 1
        else:
            temp.append(nums2[j])
            j += 1
    while i < n1:
        temp.append(nums1[i])
        i += 1
    while j < n2:
        temp.append(nums2[j])
        j += 1

    for i in range(n1 + n2):
        if i < n1:
            nums1[i] = temp[i]
        else:
            nums2[i - n1] = temp[i]

    print(nums1, nums2)
    return


def mergeArraysOptimal1(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    i = n1 - 1
    j = 0
    while i >= 0 and j < n2:
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i -= 1
            j += 1
        else:
            break
    nums1.sort()
    nums2.sort()

    print(nums1, nums2)
    return


def mergeArraysOptimal2(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    gap = (n // 2) + (n % 2)

    def swapIfGreater(arr1, arr2, index1, index2):
        if arr1[index1] > arr2[index2]:
            arr1[index1], arr2[index2] = arr2[index2], arr1[index1]

    while gap > 0:
        i = 0
        j = i + gap
        while j < n:
            # nums1 and nums2
            if i < n1 <= j:
                swapIfGreater(nums1, nums2, i, j - n1)
            # nums2 and nums2
            elif i >= n1:
                swapIfGreater(nums2, nums2, i - n1, j - n1)
            # nums1 and nums1
            else:
                swapIfGreater(nums1, nums1, i, j)
            i += 1
            j += 1
        if gap == 1: break
        gap = (gap // 2) + (gap % 2)

    print(nums1, nums2)
    return


# Gap method
# Intuition comes from Shell Sort
mergeArraysBrute([1, 3, 5, 7], [0, 2, 6, 8, 9])
mergeArraysOptimal1([1, 3, 5, 7], [0, 2, 6, 8, 9])
mergeArraysOptimal2([1, 3, 5, 7], [0, 2, 6, 8, 9])
