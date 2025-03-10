class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1, n):
            fact *= i
            nums.append(i)
        nums.append(n)

        res = ""
        k = k - 1  # Zero based indexing
        while True:
            num = nums[k // fact]
            res += str(num)
            nums.remove(num)
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact // len(nums)
        return res


s = Solution()
print(s.getPermutation(3, 3))
print(s.getPermutation(4, 9))
