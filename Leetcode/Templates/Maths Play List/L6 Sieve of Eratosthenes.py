class Solution:
    def printPrimes(self, n: int):

        primes = [1] * (n + 1)

        for i in range(2, int(n ** 0.5)): # 2 --> sqrt(n)
            if primes[i]:
                for j in range(i * i, n + 1, i): # i x i --> n + 1, step = i
                    primes[j] = 0

        res = []
        for i in range(2, n + 1):
            if primes[i]:
                res.append(i)
        print(res)


s = Solution()
s.printPrimes(30)
s.printPrimes(100)
