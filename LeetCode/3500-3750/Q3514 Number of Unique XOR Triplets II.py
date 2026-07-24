from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i, n):
                st.add(nums[i] ^ nums[j])
        res = set()
        for x in st:
            for num in nums:
                res.add(x ^ num)
        return len(res)


s = Solution()
print(s.uniqueXorTriplets(nums=[1, 2]))
print(s.uniqueXorTriplets(nums=[3, 1, 2]))
