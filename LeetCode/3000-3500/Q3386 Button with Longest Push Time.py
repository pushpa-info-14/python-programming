from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res = events[0][0]
        max_diff = events[0][1]
        for i in reversed(range(1, len(events))):
            index, time = events[i]
            diff = time - events[i - 1][1]
            if diff > max_diff or (diff == max_diff and res > index):
                max_diff = diff
                res = index
        return res


s = Solution()
print(s.buttonWithLongestTime(events=[[1, 2], [2, 5], [3, 9], [1, 15]]))
print(s.buttonWithLongestTime(events=[[10, 5], [1, 7]]))
