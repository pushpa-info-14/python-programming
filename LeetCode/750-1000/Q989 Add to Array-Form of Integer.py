from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = 0
        num.reverse()
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            carry = num[i] // 10
            num[i] %= 10
            k //= 10
            k += carry
            i += 1
        return num[::-1]


s = Solution()
print(s.addToArrayForm(num=[1, 2, 0, 0], k=34))
print(s.addToArrayForm(num=[2, 7, 4], k=181))
print(s.addToArrayForm(num=[2, 1, 5], k=806))
