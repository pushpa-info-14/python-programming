class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odd_nums = []
        even_nums = []
        for num in nums1:
            if num & 1:
                odd_nums.append(num)
            else:
                even_nums.append(num)
        if len(odd_nums) == n or len(even_nums) == n:
            return True

        # odd - odd = even
        try_even = True
        if len(odd_nums) > 0:
            try_even = False

        # even - odd = odd
        try_odd = True
        odd_nums.sort()
        if odd_nums[0] >= sorted(even_nums)[0]:
            try_odd = False
        return try_even or try_odd

    def uniformArray2(self, nums1: list[int]) -> bool:
        nums1.sort()
        if nums1[0] % 2 == 0:
            for num in nums1:
                if num % 2 == 1:
                    return False
        return True


s = Solution()
print(s.uniformArray(nums1=[2, 3]))
print(s.uniformArray(nums1=[4, 6]))
print(s.uniformArray(nums1=[11, 16]))
print("-------------")
print(s.uniformArray2(nums1=[2, 3]))
print(s.uniformArray2(nums1=[4, 6]))
print(s.uniformArray2(nums1=[11, 16]))
