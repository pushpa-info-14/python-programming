from collections import Counter, defaultdict
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_digits = sorted(set(digits))
        counter = Counter(digits)
        res = []

        def dfs(arr, freq):
            if len(arr) == 3:
                num = arr[0] * 100 + arr[1] * 10 + arr[2]
                if num % 2 == 0:
                    res.append(num)
                return
            for digit in unique_digits:
                if digit == 0 and len(arr) == 0:
                    continue
                if freq[digit] < counter[digit]:
                    freq[digit] += 1
                    arr.append(digit)
                    dfs(arr, freq)
                    freq[digit] -= 1
                    arr.pop()

        dfs([], defaultdict(int))
        return res


s = Solution()
print(s.findEvenNumbers([2, 1, 3, 0]))
print(s.findEvenNumbers([2, 2, 8, 8, 2]))
print(s.findEvenNumbers([3, 7, 5]))
