from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = int(1e9 + 7)
        res = 0
        for i in range(n):
            mini = arr[i]
            for j in range(i, n):
                mini = min(mini, arr[j])
                res = (res + mini) % mod
        return res

    def find_next_smaller_element(self, arr):
        n = len(arr)
        nse = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        return nse

    def find_previous_smaller_or_equal_element(self, arr):
        n = len(arr)
        psee = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                psee[i] = stack[-1]
            stack.append(i)
        return psee

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        n = len(arr)
        mod = int(1e9 + 7)
        nse = self.find_next_smaller_element(arr)
        psee = self.find_previous_smaller_or_equal_element(arr)
        res = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            res = (res + left * right * arr[i]) % mod
        return res


s = Solution()
print(s.sumSubarrayMins([3, 1, 2, 4]))  # 17
print(s.sumSubarrayMins([11, 81, 94, 43, 3]))  # 444

print(s.sumSubarrayMins2([3, 1, 2, 4]))  # 17
print(s.sumSubarrayMins2([11, 81, 94, 43, 3]))  # 444
