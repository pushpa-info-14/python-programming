from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        match = 0

        i, j = 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
            elif players[i] > trainers[j]:
                j += 1
            else:
                i += 1
        return match


s = Solution()
print(s.matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))
print(s.matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]))
