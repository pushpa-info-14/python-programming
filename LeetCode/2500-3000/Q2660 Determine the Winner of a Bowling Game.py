from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        score1 = 0
        score2 = 0
        for i in range(n):
            cur1 = player1[i]
            cur2 = player2[i]
            if i > 0:
                if player1[i - 1] == 10:
                    cur1 = 2 * player1[i]
                if player2[i - 1] == 10:
                    cur2 = 2 * player2[i]
            if i > 1:
                if player1[i - 2] == 10:
                    cur1 = 2 * player1[i]
                if player2[i - 2] == 10:
                    cur2 = 2 * player2[i]
            score1 += cur1
            score2 += cur2

        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0


s = Solution()
print(s.isWinner(player1=[5, 10, 3, 2], player2=[6, 5, 7, 3]))
print(s.isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
print(s.isWinner(player1=[2, 3], player2=[4, 1]))
print(s.isWinner(player1=[1, 1, 1, 10, 10, 10, 10], player2=[10, 10, 10, 10, 1, 1, 1]))
