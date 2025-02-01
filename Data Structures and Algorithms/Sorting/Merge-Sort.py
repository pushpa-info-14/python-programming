def merge(a, b):
    len_a = len(a)
    len_b = len(b)

    c = []
    i, j = 0, 0
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len_a:
        c.append(a[i])
        i += 1
    while j < len_b:
        c.append(b[j])
        j += 1
    return c


def merge_sort(l, r):
    if l < r:
        mid = (l + r) // 2
        a = merge_sort(l, mid)
        b = merge_sort(mid + 1, r)
        return merge(a, b)
    return [array[l]]


array = [9, 3, 7, 5, 6, 4, 8, 2]
n = len(array)
print(merge_sort(0, n - 1))
