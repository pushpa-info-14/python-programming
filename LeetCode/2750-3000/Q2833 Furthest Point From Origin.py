class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count, r_count, any_count = 0, 0, 0
        for move in moves:
            if move == "L":
                l_count += 1
            elif move == "R":
                r_count += 1
            else:
                any_count += 1
        return any_count + abs(l_count - r_count)


s = Solution()
print(s.furthestDistanceFromOrigin(moves="L_RL__R"))
print(s.furthestDistanceFromOrigin(moves="_R__LL_"))
print(s.furthestDistanceFromOrigin(moves="_______"))
