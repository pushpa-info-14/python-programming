from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def get_primes(n):
            is_prime = [1] * (n + 1)
            is_prime[0] = 0
            is_prime[1] = 0

            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i] == 1:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = 0
            temp = []
            for i in range(left, right + 1):
                if is_prime[i]:
                    temp.append(i)
            return temp

        primes = get_primes(right)
        res = [-1, -1]
        diff = right - left + 1
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]
        return res


s = Solution()
print(s.closestPrimes(10, 19))
print(s.closestPrimes(4, 6))
