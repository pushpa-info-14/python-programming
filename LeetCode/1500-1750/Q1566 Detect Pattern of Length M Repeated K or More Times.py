from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m * k:
            return False
        for i in range(n - m * k + 1):
            count = 0
            pattern = []
            for j in range(i, i + m):
                pattern.append(arr[j])
            count += 1

            for j in range(k - 1):
                start = i + m + j * m
                p = []
                for x in range(start, start + m):
                    p.append(arr[x])
                if p == pattern:
                    count += 1
                else:
                    break
            if count == k:
                return True
        return False

    def containsPattern2(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        count = 0
        for i in range(n - m):
            if arr[i] == arr[i + m]:
                count += 1
                if count == m * (k - 1):
                    return True
            else:
                count = 0
        return False


s = Solution()
print(s.containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(s.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(s.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
print(s.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(s.containsPattern(arr=[2, 2], m=1, k=2))
print(s.containsPattern2(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(s.containsPattern2(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(s.containsPattern2(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
print(s.containsPattern2(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(s.containsPattern2(arr=[2, 2], m=1, k=2))
