from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = []
        while True:
            flag = True
            bit_count = 0
            for i in range(n):
                num = nums[i]
                if num > 0:
                    flag = False
                bit_count += num % 2
                nums[i] = num // 2
            if flag:
                break
            if bit_count >= k:
                bits.append(1)
            else:
                bits.append(0)
        res = 0
        for bit in bits[::-1]:
            res = (res << 1) + bit
        return res


s = Solution()
print(s.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
print(s.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6))
print(s.findKOr(nums=[10, 8, 5, 9, 11, 6, 8], k=1))
print(s.findKOr(nums=[14, 7, 12, 9, 8, 9, 1, 15], k=4))
