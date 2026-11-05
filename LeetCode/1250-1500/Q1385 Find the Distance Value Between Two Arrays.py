import bisect


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for x in arr1:
            flag = True
            for y in arr2:
                if abs(x - y) <= d:
                    flag = False
                    break
            if flag:
                res += 1
        return res

    def findTheDistanceValue2(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n = len(arr2)
        arr2.sort()
        res = 0
        for num in arr1:
            i = bisect.bisect_left(arr2, num)
            if i == n or abs(num - arr2[i]) > d:
                if i == 0 or abs(num - arr2[i - 1]) > d:
                    res += 1
        return res


s = Solution()
print(s.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
print(s.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(s.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
print("-------------------------")
print(s.findTheDistanceValue2(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
print(s.findTheDistanceValue2(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(s.findTheDistanceValue2(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
