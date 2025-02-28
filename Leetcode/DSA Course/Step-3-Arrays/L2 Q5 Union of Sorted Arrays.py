def union(nums1, nums2):
    s = set()
    for num in nums1:
        s.add(num)
    for num in nums2:
        s.add(num)

    return list(s)


def union2(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    res = []

    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            while i < n1 and nums1[i] == res[-1]:
                i += 1
        elif nums1[i] > nums2[j]:
            res.append(nums2[j])
            while j < n1 and nums2[j] == res[-1]:
                j += 1
        else:
            res.append(nums1[i])
            while i < n1 and nums1[i] == res[-1]:
                i += 1
            while j < n1 and nums2[j] == res[-1]:
                j += 1
    while i < n1:
        if res[-1] < nums1[i]:
            res.append(nums1[i])
        i += 1

    while j < n2:
        if res[-1] < nums2[j]:
            res.append(nums2[j])
        j += 1

    return res


print(union([1, 1, 2, 3, 4, 5], [2, 3, 4, 4, 5, 6]))
print(union2([1, 1, 2, 3, 4, 5], [2, 3, 4, 4, 5, 6]))
