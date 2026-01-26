class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        splits = s.split(' ')
        for x in splits:
            if x.isnumeric():
                num = int(x)
                if num <= prev:
                    return False
                prev = num
        return True


s = Solution()
print(s.areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(s.areNumbersAscending(s="hello world 5 x 5"))
print(s.areNumbersAscending(s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
