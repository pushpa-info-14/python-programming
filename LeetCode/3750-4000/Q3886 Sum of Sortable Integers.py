class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if n // i != i:
                    divisors.append(n // i)
        res = 0
        inf = 10 ** 10
        for k in divisors:
            prev_max = 0
            flag = True
            cur = 0
            while cur < n:
                segment = []
                cur_min, cur_max = inf, -inf
                for i in range(cur, cur + k):
                    segment.append(nums[i])
                    cur_min = min(cur_min, nums[i])
                    cur_max = max(cur_max, nums[i])
                if prev_max > cur_min:
                    flag = False
                    break
                count = 0
                for i in range(k):
                    if segment[i] > segment[(i + 1) % k]:
                        count += 1
                if count > 1:
                    flag = False
                    break
                prev_max = cur_max
                cur += k
            if flag:
                res += k
        return res


s = Solution()
print(s.sortableIntegers(nums=[3, 1, 2]))
print(s.sortableIntegers(nums=[7, 6, 5]))
print(s.sortableIntegers(nums=[5, 8]))
print(s.sortableIntegers(nums=[1, 2, 3]))
print(s.sortableIntegers(nums=[12, 18, 14]))
