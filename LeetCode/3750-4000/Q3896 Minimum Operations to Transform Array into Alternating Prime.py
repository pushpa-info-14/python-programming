import bisect

primes = []
for n in range(2, 10 ** 5 + 10):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
    if cnt == 2:
        primes.append(n)


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                idx = bisect.bisect_left(primes, num)
                if primes[idx] != num:
                    res += (primes[idx] - num)
            else:
                if num == 2:
                    res += 2
                else:
                    idx = bisect.bisect_left(primes, num)
                    if primes[idx] == num:
                        res += 1
        return res


s = Solution()
print(s.minOperations(nums=[1, 2, 3, 4]))
print(s.minOperations(nums=[5, 6, 7, 8]))
print(s.minOperations(nums=[4, 4]))
