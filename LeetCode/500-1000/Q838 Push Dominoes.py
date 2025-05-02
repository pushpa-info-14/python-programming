class Domino:
    def doubleDominoPush(self, last_r, pos, dominoes_list):
        while last_r < pos:
            dominoes_list[last_r] = 'R'
            dominoes_list[pos] = 'L'
            last_r += 1
            pos -= 1

    def leftDominoPush(self, start, end, dominoes_list):
        while start <= end:
            dominoes_list[start] = 'L'
            start += 1

    def rightDominoPush(self, last_r, pos, dominoes_list):
        while last_r <= pos:
            dominoes_list[last_r] = 'R'
            last_r += 1


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dominoes_list = list(dominoes)
        domino = Domino()
        last_l = -1
        last_r = -1
        for pos in range(n):
            if dominoes_list[pos] == 'L':
                if last_r > last_l:
                    domino.doubleDominoPush(last_r, pos, dominoes_list)
                elif (last_l > last_r) or (last_l == -1):
                    domino.leftDominoPush(last_l + 1, pos, dominoes_list)
                last_l = pos
            elif dominoes_list[pos] == 'R':
                if last_r > last_l:
                    domino.rightDominoPush(last_r, pos, dominoes_list)
                last_r = pos

        # Final case: (R)RR...R(end)
        if last_r > last_l:
            domino.rightDominoPush(last_r, n - 1, dominoes_list)

        return "".join(dominoes_list)


s = Solution()
print(s.pushDominoes(dominoes="RR.L"))
print(s.pushDominoes(dominoes=".L.R...LR..L.."))
print(s.pushDominoes(dominoes=".L.R."))  # "LL.RR"
