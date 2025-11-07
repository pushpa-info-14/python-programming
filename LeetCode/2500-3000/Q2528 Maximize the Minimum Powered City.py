from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i in range(n):
            left = max(i - r, 0)
            right = min(i + r + 1, n)
            diff[left] += stations[i]
            diff[right] -= stations[i]

        def can_achieve(target_p):
            cur_p = 0
            cur_k = k
            diff_copy = diff.copy()
            for _i in range(n):
                cur_p += diff_copy[_i]
                if cur_p < target_p:
                    additional = target_p - cur_p
                    if additional > cur_k:
                        return False
                    cur_k -= additional
                    cur_p += additional
                    _right = min(_i + 2 * r + 1, n)
                    diff_copy[_right] -= additional
            return True

        low, high = min(stations), sum(stations) + k
        res = low
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


s = Solution()
print(s.maxPower(stations=[1, 2, 4, 5, 0], r=1, k=2))
print(s.maxPower(stations=[4, 4, 4, 4], r=0, k=3))
