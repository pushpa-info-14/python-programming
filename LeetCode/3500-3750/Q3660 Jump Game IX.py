from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        st = []

        for i in range(n):
            v = nums[i]
            l, r = i, i
            while st and st[-1][0] > nums[i]:
                last_v, last_l, last_r = st.pop()
                v = max(v, last_v)
                l = last_l
            st.append((v, l, r))

        for v, l, r in st:
            for i in range(l, r + 1):
                res[i] = v
        return res


s = Solution()
print(s.maxValue(nums=[2, 1, 3]))
print(s.maxValue(nums=[2, 3, 1]))
