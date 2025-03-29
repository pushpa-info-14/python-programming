from heapq import heapify, heappop
from math import sqrt
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        res = 1

        prime_scores = []
        for num in nums:
            score = 0
            for f in range(2, int(sqrt(num)) + 1):
                if num % f == 0:
                    score += 1
                    while num % f == 0:
                        num = num // f
            if num > 1:
                score += 1
            prime_scores.append(score)

        left_bound = [-1] * n
        right_bound = [n] * n
        stack = []
        for i, score in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < score:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)

        min_heap = [(-num, i) for i, num in enumerate(nums)]
        heapify(min_heap)

        while k > 0:
            num, index = heappop(min_heap)
            num = -num

            left_count = index - left_bound[index]
            right_count = right_bound[index] - index
            count = left_count * right_count
            operations = min(count, k)
            res = (res * pow(num, operations, mod)) % mod
            k -= operations
        return res


s = Solution()
print(s.maximumScore(nums=[8, 3, 9, 3, 8], k=2))
print(s.maximumScore(nums=[19, 12, 14, 6, 10, 18], k=3))
