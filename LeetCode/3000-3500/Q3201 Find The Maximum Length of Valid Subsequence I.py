from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        last = -1
        flips = evens = 0
        for n in nums:
            if last != n % 2:
                flips += 1
            if n % 2:
                evens += 1
            last = n % 2
        return max(flips, evens, len(nums) - evens)

    def maximumLength2(self, nums: List[int]) -> int:
        n = len(nums)
        odd_count = 1 if nums[0] % 2 == 1 else 0
        even_count = 1 if nums[0] % 2 == 0 else 0
        alternate_count = 1
        expecting_even = True if nums[0] % 2 == 1 else False
        """
            True: expecting EVEN as next number in sequence
            False: expecting ODD as next number in sequence
        """
        for i in range(1, n):
            if (expecting_even == True and nums[i] % 2 == 0) or (expecting_even == False and nums[i] % 2 == 1):
                alternate_count += 1
                expecting_even = not expecting_even

            if nums[i] % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
        return max(even_count, odd_count, alternate_count)


s = Solution()
print(s.maximumLength(nums=[1, 2, 3, 4]))
print(s.maximumLength(nums=[1, 2, 1, 1, 2, 1, 2]))
print(s.maximumLength(nums=[1, 3]))
print(s.maximumLength2(nums=[1, 2, 3, 4]))
print(s.maximumLength2(nums=[1, 2, 1, 1, 2, 1, 2]))
print(s.maximumLength2(nums=[1, 3]))
