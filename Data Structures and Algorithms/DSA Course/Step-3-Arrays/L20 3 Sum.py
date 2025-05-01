from typing import List


class Solution:
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hashset = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if cur_sum == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        hashset.add(tuple(temp))
        return [list(i) for i in hashset]

    def threeSumBetter(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            hashset = set()
            for j in range(i, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    res.add(tuple(temp))
                hashset.add(nums[j])
        return [list(i) for i in res]

    def threeSumOptimal1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

    def threeSumOptimal2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res


s = Solution()
print(s.threeSumBrute([-1, -1, 2, 0, 1]))
print(s.threeSumBetter([-1, -1, 2, 0, 1]))
print(s.threeSumOptimal1([-1, -1, 2, 0, 1]))
print(s.threeSumOptimal2([-1, -1, 2, 0, 1]))
