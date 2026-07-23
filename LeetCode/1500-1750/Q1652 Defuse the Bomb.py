from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        prefix_sum = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix_sum[i + 1] = code[i % n] + prefix_sum[i]
        for i in range(n):
            if k == 0:
                code[i] = 0
            elif k > 0:
                code[i] = prefix_sum[i + k + 1] - prefix_sum[i + 1]
            else:
                code[i] = prefix_sum[n + i] - prefix_sum[n + i + k]
        return code


s = Solution()
print(s.decrypt(code=[5, 7, 1, 4], k=3))
print(s.decrypt(code=[1, 2, 3, 4], k=0))
print(s.decrypt(code=[2, 4, 9, 3], k=-2))
