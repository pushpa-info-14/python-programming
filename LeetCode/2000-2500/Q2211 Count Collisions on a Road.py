class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        n = len(directions)
        res = 0
        r_count = 1 if directions[0] == 'R' else 0
        for i in range(1, n):
            if directions[i] == 'R':
                r_count += 1
            if directions[i - 1] == 'R' and directions[i] == 'S':
                res += r_count
                directions[i] = 'S'
            elif directions[i - 1] == 'R' and directions[i] == 'L':
                res += r_count + 1
                directions[i] = 'S'
            elif directions[i - 1] == 'S' and directions[i] == 'L':
                res += 1
                directions[i] = 'S'

            if directions[i] != 'R':
                r_count = 0
        return res

    def countCollisions2(self, directions: str) -> int:
        dirs = directions.lstrip("L").rstrip("R")
        return len(dirs) - dirs.count("S")


s = Solution()
print(s.countCollisions(directions="RLRSLL"))
print(s.countCollisions(directions="LLRR"))
print(s.countCollisions(directions="SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"))
print(s.countCollisions2(directions="RLRSLL"))
print(s.countCollisions2(directions="LLRR"))
print(s.countCollisions2(directions="SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"))
