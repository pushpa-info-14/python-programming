from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        self.seg_tree = [0] * (4 * n + 1)

        nums2_val_idx = {val: idx for idx, val in enumerate(nums2)}

        def update_seg_tree(st_idx, start, end, query_idx):
            if end < query_idx or start > query_idx:
                return
            if start == end:
                self.seg_tree[st_idx] += 1
                return
            mid = start + (end - start) // 2
            update_seg_tree(2 * st_idx, start, mid, query_idx)
            update_seg_tree(2 * st_idx + 1, mid + 1, end, query_idx)
            self.seg_tree[st_idx] = self.seg_tree[2 * st_idx] + self.seg_tree[2 * st_idx + 1]

        def range_sum_query(st_idx, start, end, qs, qe):
            if qs > end or qe < start:
                return 0
            if start >= qs and end <= qe:
                return self.seg_tree[st_idx]
            mid = start + (end - start) // 2
            left_sum = range_sum_query(2 * st_idx, start, mid, qs, qe)
            right_sum = range_sum_query(2 * st_idx + 1, mid + 1, end, qs, qe)
            return left_sum + right_sum

        update_seg_tree(1, 0, n - 1, nums2_val_idx[nums1[0]])

        count_good_triplets = 0
        for i in range(1, n - 1):
            nums2_idx = nums2_val_idx[nums1[i]]
            common_left_elements = range_sum_query(1, 0, n - 1, 0, nums2_idx)
            uncommon_left_items = i - common_left_elements
            common_right_elements = (n - nums2_idx - 1) - uncommon_left_items
            count_good_triplets += common_left_elements * common_right_elements

            update_seg_tree(1, 0, n - 1, nums2_idx)

        return count_good_triplets


s = Solution()
print(s.goodTriplets(nums1=[2, 0, 1, 3], nums2=[0, 1, 2, 3]))
print(s.goodTriplets(nums1=[4, 0, 1, 3, 2], nums2=[4, 1, 0, 2, 3]))
