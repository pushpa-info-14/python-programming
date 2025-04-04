from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        def merge(arr, l, m, r):
            left, right = arr[l:m + 1], arr[m + 1:r + 1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
            return arr

        return merge_sort(nums, 0, len(nums) - 1)


s = Solution()
print(s.sortArray([5, 2, 3, 1]))
