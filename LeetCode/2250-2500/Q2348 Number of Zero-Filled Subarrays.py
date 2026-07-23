from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        counter = 0
        for num in nums:
            if num == 0:
                counter += 1
            else:
                if counter != 0:
                    res += counter * (counter + 1) // 2
                    counter = 0
        res += counter * (counter + 1) // 2
        return res


s = Solution()
print(s.zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4]))
print(s.zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
print(s.zeroFilledSubarray(nums=[2, 10, 2019]))
