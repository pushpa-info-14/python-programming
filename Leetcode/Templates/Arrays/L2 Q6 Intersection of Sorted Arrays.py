def intersection(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    res = []

    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res


print(intersection([1, 2, 2, 3, 3, 4, 5, 6], [2, 3, 3, 5, 6, 6, 7]))
