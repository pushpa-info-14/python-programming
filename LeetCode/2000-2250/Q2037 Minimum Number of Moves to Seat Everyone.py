from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        res = 0
        for i in range(n):
            res += abs(seats[i] - students[i])
        return res


s = Solution()
print(s.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
print(s.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(s.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
