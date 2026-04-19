class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        mod = 10 ** 9 + 7
        pairs = []
        edge_cases = []
        for ones, zeros in zip(nums1, nums0):
            if zeros == 0:
                edge_cases.append(ones)
            else:
                pairs.append([ones, zeros])
        pairs.sort(key=lambda x: (-x[0], x[1]))
        res = 0
        if edge_cases:
            res = pow(2, sum(edge_cases), mod) - 1
        for ones, zeros in pairs:
            x = pow(2, ones, mod) - 1
            y = x << zeros
            res <<= (ones + zeros)
            res += y
            res %= mod
        return res


s = Solution()
print(s.maxValue(nums1=[1, 2], nums0=[1, 0]))
print(s.maxValue(nums1=[3, 1], nums0=[0, 3]))
print(s.maxValue(
    nums1=[4666, 4480, 9564, 3035, 4980, 7661, 278, 409, 1885, 5, 1354, 2885, 7716, 7156, 5, 6600, 4806, 2172, 680,
           1209, 8821, 8893],
    nums0=[8623, 2632, 10000, 10000, 10000, 443, 214, 31, 10000, 6, 7974, 8100, 3414, 241, 447, 4177, 10000, 1313, 6219,
           10000, 1248, 5622]))
