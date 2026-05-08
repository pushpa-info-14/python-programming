from collections import defaultdict, deque
from typing import List

mx = 10 ** 6 + 1
primes = [True] * mx
primes[0], primes[1] = False, False
spf = [0] * mx
for i in range(2, mx):
    if primes[i]:
        spf[i] = i
        for j in range(i * i, mx, i):
            primes[j] = False
            if spf[j] == 0:
                spf[j] = i


def factors(x):
    res = set()
    while x > 1:
        p = spf[x]
        res.add(p)
        x //= p
    return res


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        groups = defaultdict(list)

        for i, num in enumerate(nums):
            for p in factors(num):
                groups[p].append(i)

        q = deque()
        q.append((0, 0))  # i, jumps
        seen_i = set()
        seen_i.add(0)
        seen_p = set()

        while q:
            i, jumps = q.popleft()
            if i == n - 1:
                return jumps
            if i + 1 < n and i + 1 not in seen_i:
                q.append((i + 1, jumps + 1))
                seen_i.add(i + 1)
            if i - 1 >= 0 and i - 1 not in seen_i:
                q.append((i - 1, jumps + 1))
                seen_i.add(i - 1)
            if nums[i] in groups and nums[i] not in seen_p:
                seen_p.add(nums[i])
                for j in groups[nums[i]]:
                    if j not in seen_i:
                        q.append((j, jumps + 1))
                        seen_i.add(j)
        return 0


s = Solution()
print(s.minJumps(nums=[1, 2, 4, 6]))
print(s.minJumps(nums=[2, 3, 4, 7, 9]))
print(s.minJumps(nums=[4, 6, 5, 8]))
