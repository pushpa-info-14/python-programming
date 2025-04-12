from typing import List


class Solution:
    def __init__(self):
        self.fact = [0] * 11
        self.done = set()
        self.k_palindromes = 0
        self.preComputeFactorial()

    def preComputeFactorial(self):
        self.fact[0] = 1
        self.fact[1] = 1
        for i in range(2, 11):
            self.fact[i] = i * self.fact[i - 1]

    def countAllPermutations(self, freq: List[int], n):
        count = self.fact[n]
        for i in range(10):
            count //= self.fact[freq[i]]
        return count

    def allArrangements(self, number: List[str], n: int):
        # number.sort() You cannot do. You update the array. Take a copy
        sorted_num = ''.join(sorted(number))
        num = int(sorted_num)
        if num in self.done:
            return 0

        self.done.add(num)

        # Find the frequency of each digit
        freq = [0] * 10
        for i in number:
            freq[int(i)] += 1

        total_permutations = self.countAllPermutations(freq, n)
        invalid_permutations = 0
        if freq[0] > 0:
            freq[0] -= 1
            invalid_permutations = self.countAllPermutations(freq, n - 1)
        return total_permutations - invalid_permutations

    @staticmethod
    def isKPalindrome(number: str, k):
        return int(number) % k == 0

    def generatePalindromes(self, index, n, number: List[str], k):
        if index >= (n + 1) // 2:
            # print(number)
            if self.isKPalindrome("".join(number), k):
                self.k_palindromes += self.allArrangements(number, n)
            return

        start = 1 if index == 0 else 0
        while start <= 9:
            number[index] = str(start)
            number[n - index - 1] = str(start)
            self.generatePalindromes(index + 1, n, number, k)
            start += 1
        number[index] = ' '

    def countGoodIntegers(self, n: int, k: int) -> int:
        self.done = set()
        self.k_palindromes = 0
        number = [' '] * n
        self.generatePalindromes(0, n, number, k)

        return self.k_palindromes


s = Solution()
print(s.countGoodIntegers(3, 5))
print(s.countGoodIntegers(1, 4))
print(s.countGoodIntegers(5, 6))
