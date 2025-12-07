from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        arr = []
        res = 0
        count = 0
        for x in flowerbed:
            if x == 0:
                count += 1
            elif count:
                arr.append(count)
                res += (count + 1) // 2 - 1
                count = 0
        if count:
            arr.append(count)
            res += (count + 1) // 2 - 1
        return res >= n


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2))
