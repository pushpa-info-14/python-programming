from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        top = SortedList()  # (freq, num)
        remain = SortedList()  # (freq, num)
        res = []
        cur_sum = 0

        def balance():
            nonlocal cur_sum

            if len(top) < x and remain:
                f, num = remain.pop()
                top.add((f, num))
                cur_sum += f * num

            if top and remain and remain[-1] > top[0]:
                f1, num1 = top.pop(0)
                f2, num2 = remain.pop()
                top.add((f2, num2))
                remain.add((f1, num1))
                cur_sum -= f1 * num1
                cur_sum += f2 * num2

        def update(num, delta):
            nonlocal cur_sum
            if num in freq:
                if (freq[num], num) in top:
                    top.remove((freq[num], num))
                    cur_sum -= freq[num] * num
                else:
                    remain.remove((freq[num], num))
            freq[num] += delta
            if freq[num] == 0:
                del freq[num]
            else:
                remain.add((freq[num], num))
            balance()

        for i in range(k):
            update(nums[i], 1)
        res.append(cur_sum)
        for i in range(k, n):
            update(nums[i - k], -1)
            update(nums[i], 1)
            res.append(cur_sum)
        return res


s = Solution()
print(s.findXSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
print(s.findXSum(nums=[3, 8, 7, 8, 7, 5], k=2, x=2))
print(s.findXSum(nums=[9, 2, 2], k=3, x=3))
print(s.findXSum(nums=[3, 7, 10, 5, 5], k=2, x=2))
print(s.findXSum(nums=[6, 1, 10, 6, 7], k=4, x=4))
