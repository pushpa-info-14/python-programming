from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        steps = n
        for i in [tops[0], bottoms[0]]:
            top = 0
            bottom = 0
            for j in range(n):
                if tops[j] != i and bottoms[j] != i:
                    top = -1
                    bottom = -1
                    break
                if tops[j] != i and bottoms[j] == i:
                    top += 1
                elif tops[j] == i and bottoms[j] != i:
                    bottom += 1
            if top != -1:
                steps = min(steps, top)
            if bottom != -1:
                steps = min(steps, bottom)

        return steps if steps != n else -1

    def minDominoRotations2(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def check(num, arr1, arr2):
            steps = 0
            for j in range(n):
                if arr1[j] != num and arr2[j] != num:
                    return len(arr1)
                if arr1[j] != num and arr2[j] == num:
                    steps += 1
            return steps

        res1 = min(check(tops[0], tops, bottoms), check(tops[0], bottoms, tops))
        res2 = min(check(bottoms[0], tops, bottoms), check(bottoms[0], bottoms, tops))
        res = min(res1, res2)

        return res if res != n else -1


s = Solution()
print(s.minDominoRotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
print(s.minDominoRotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
print(s.minDominoRotations(tops=[1, 2, 1, 1, 1, 2, 2, 2], bottoms=[2, 1, 2, 2, 2, 2, 2, 2]))
print(s.minDominoRotations2(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
print(s.minDominoRotations2(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
print(s.minDominoRotations2(tops=[1, 2, 1, 1, 1, 2, 2, 2], bottoms=[2, 1, 2, 2, 2, 2, 2, 2]))
