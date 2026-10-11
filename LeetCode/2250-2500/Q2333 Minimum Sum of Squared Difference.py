from collections import defaultdict


class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        freq = defaultdict(int)
        for a, b in zip(nums1, nums2):
            freq[abs(a - b)] += 1
        k = k1 + k2
        for diff in range(max(freq.keys()), 0, -1):
            if freq[diff] == 0:
                continue
            mn = min(k, freq[diff])
            k -= mn
            freq[diff] -= mn
            freq[diff - 1] += mn
        res = 0
        for diff in freq.keys():
            if freq[diff] > 0:
                res += (diff ** 2) * freq[diff]
        return res

    def minSumSquareDiff2(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        diffs.sort(reverse=True)
        diffs.append(0)
        k = k1 + k2
        for i in range(n):
            d = diffs[i] - diffs[i + 1]
            if d * (i + 1) < k:
                k -= d * (i + 1)
            else:
                q, r = divmod(k, i + 1)
                out = sum(diffs[j] ** 2 for j in range(i + 1, n))
                out += (((diffs[i] - q) - 1) ** 2) * r
                out += ((diffs[i] - q) ** 2) * (i + 1 - r)
                return out
        return 0


s = Solution()
print(s.minSumSquareDiff(nums1=[1, 2, 3, 4], nums2=[2, 10, 20, 19], k1=0, k2=0))
print(s.minSumSquareDiff(nums1=[1, 4, 10, 12], nums2=[5, 8, 6, 9], k1=1, k2=1))
print("---------")
print(s.minSumSquareDiff2(nums1=[1, 2, 3, 4], nums2=[2, 10, 20, 19], k1=0, k2=0))
print(s.minSumSquareDiff2(nums1=[1, 4, 10, 12], nums2=[5, 8, 6, 9], k1=1, k2=1))
