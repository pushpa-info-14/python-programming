from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        prefix_max = [0] * n
        suffix_max = [0] * n

        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        suffix_max[n - 1] = height[n - 1]
        for i in reversed(range(n - 1)):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        for i in range(n):
            if height[i] < prefix_max[i] and height[i] < suffix_max[i]:
                res += min(prefix_max[i], suffix_max[i]) - height[i]

        return res

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        prefix_max = height[0]
        suffix_max = [0] * n

        suffix_max[n - 1] = height[n - 1]
        for i in reversed(range(n - 1)):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        for i in range(n):
            prefix_max = max(prefix_max, height[i])
            if height[i] < prefix_max and height[i] < suffix_max[i]:
                res += min(prefix_max, suffix_max[i]) - height[i]

        return res

    def trap3(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l_max = 0
        r_max = 0
        l, r = 0, n - 1

        while l < r:
            if height[l] < height[r]:
                if height[l] < l_max:
                    res += l_max - height[l]
                else:
                    l_max = max(l_max, height[l])
                l += 1
            else:
                if height[r] < r_max:
                    res += r_max - height[r]
                else:
                    r_max = max(r_max, height[r])
                r -= 1
        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))

print(s.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap2([4, 2, 0, 3, 2, 5]))

print(s.trap3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap3([4, 2, 0, 3, 2, 5]))
