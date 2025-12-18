from typing import List


class Solution:
    def tallest_possible_stack_height(self, boxes: List[List[int]]) -> int:
        n = len(boxes)
        boxes.sort()
        dp = [i[2] for i in boxes]
        for i in range(1, n):  # Starts from 1 and look back
            for j in range(i):
                if boxes[j][0] < boxes[i][0] and boxes[j][1] < boxes[i][1]:
                    dp[i] = max(dp[i], boxes[i][2] + dp[j])
        print(dp)
        return dp[n - 1]


"""
Given n boxes [[L1,W1,H1],....,[Ln,Wn,Hn]] where box i has length Li, width Wi, and height Hi, find the 
height of the tallest possible stack. Box [Li,Wi,Hi] can be on top of box [Lj,Wj,Hj] if Li < Lj, Wi < Wj.
"""

s = Solution()
print(s.tallest_possible_stack_height([[4, 5, 3], [2, 3, 2], [3, 6, 2], [1, 5, 4], [2, 4, 1], [1, 2, 2]]))
