from typing import List


def numOfStudents(pages, max_pages):
    students = 1
    current_pages = 0
    for i in range(len(pages)):
        if current_pages + pages[i] <= max_pages:
            current_pages += pages[i]
        else:
            students += 1
            current_pages = pages[i]
    return students


def allocateBooks(pages: List[int], m):
    n = len(pages)
    if n < m: return -1

    low, high = max(pages), sum(pages)
    for i in range(low, high):
        if numOfStudents(pages, i) <= m:
            return i
    return -1


def allocateBooks2(pages: List[int], m):
    n = len(pages)
    if n < m: return -1

    low, high = max(pages), sum(pages)
    while low <= high:
        mid = (low + high) // 2
        if numOfStudents(pages, mid) <= m:
            high = mid - 1
        else:
            low = mid + 1
    return low


# Each student should gets at least one book
# Each book should be allocated to only one student
# Book allocation should be in a contiguous manner
print(allocateBooks([25, 46, 28, 49, 24], 4))
print(allocateBooks([10, 20, 30, 40], 2))
print(allocateBooks2([25, 46, 28, 49, 24], 4))
print(allocateBooks2([10, 20, 30, 40], 2))
