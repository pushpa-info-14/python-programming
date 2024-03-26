class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = str(int(n) - 1)
        result1 = [c for c in n]
        result2 = [c for c in n]

        for i in range(int(len(n) / 2)):
            if n[i] != n[-i-1]:
                if n[i] > n[-i-1]:
                    result1[i] = n[-i-1]
                    result2[-i-1] = n[i]
                else:
                    result1[-i-1] = n[i]
                    result2[i] = n[-i-1]

        dif1 = abs(int(n) - int("".join(result1)))
        dif2 = abs(int(n) - int("".join(result2)))

        print(result1)
        print(result2)

        if dif1 < dif2:
            return "".join(result1)
        else:
            return "".join(result2)


solution = Solution()
print(solution.nearestPalindromic("1213"))
